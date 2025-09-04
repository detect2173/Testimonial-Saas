import uuid
from django.conf import settings
from django.db import models

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class WallConfig(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name="wall_config")
    theme = models.CharField(max_length=20, default="light")
    primary_color = models.CharField(max_length=7, default="#111827")
    layout = models.CharField(max_length=20, default="grid")
    show_avatars = models.BooleanField(default=True)
    show_ratings = models.BooleanField(default=True)
    max_items = models.PositiveIntegerField(default=50)

class Testimonial(models.Model):
    STATUS_CHOICES = [("pending","Pending"),("approved","Approved"),("rejected","Rejected")]
    MEDIA_CHOICES = [("text","Text"),("video","Video"),("audio","Audio")]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="testimonials")
    author_name = models.CharField(max_length=120, blank=True)
    author_title = models.CharField(max_length=120, blank=True)
    author_company = models.CharField(max_length=120, blank=True)
    author_avatar_url = models.URLField(blank=True)

    content_text = models.TextField(blank=True)
    media_type = models.CharField(max_length=10, choices=MEDIA_CHOICES, default="text")
    media_url = models.URLField(blank=True)
    rating = models.PositiveSmallIntegerField(null=True, blank=True)
    source = models.CharField(max_length=50, default="link")

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-approved_at", "-created_at"]
