from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods
from .models import Project, Testimonial

@require_http_methods(["GET","POST"])
def submit_testimonial(request, slug):
    project = get_object_or_404(Project, slug=slug)
    if request.method == "POST":
        author_name = request.POST.get("author_name", "")
        content_text = request.POST.get("content_text", "")
        rating = request.POST.get("rating") or None
        Testimonial.objects.create(
            project=project,
            author_name=author_name[:120],
            content_text=content_text,
            rating=int(rating) if rating else None,
            media_type="text",
            status="pending",
            source="link",
        )
        return render(request, "thank_you.html", {"project": project})
    return render(request, "submit.html", {"project": project})


def public_wall(request, slug):
    project = get_object_or_404(Project, slug=slug)
    max_items = project.wall_config.max_items if hasattr(project, 'wall_config') else 50
    approved = project.testimonials.filter(status="approved")[: max_items]
    return render(request, "wall.html", {"project": project, "testimonials": approved})


def embed_script(request, slug):
    wall_url = request.build_absolute_uri(f"/t/{slug}/wall")
    js = f"""
    (function(){
      var d=document; var s=d.currentScript; var iframe=d.createElement('iframe');
      iframe.src='{wall_url}';
      iframe.loading='lazy';
      iframe.style.width='100%'; iframe.style.border='0'; iframe.setAttribute('data-testimonial-wall','1');
      function resize(){ try{ iframe.style.height = iframe.contentWindow.document.body.scrollHeight + 'px'; }catch(e){} }
      iframe.addEventListener('load', function(){ resize(); });
      s.parentNode.insertBefore(iframe, s);
    })();
    """
    return HttpResponse(js, content_type="application/javascript")
