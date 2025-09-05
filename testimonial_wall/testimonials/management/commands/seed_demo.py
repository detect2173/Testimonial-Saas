from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from testimonials.models import Project, WallConfig, Testimonial

class Command(BaseCommand):
    help = "Seed a demo user, project, wall config, and a sample approved testimonial."

    def handle(self, *args, **options):
        User = get_user_model()
        # Create or get demo superuser
        demo_email = "demo@example.com"
        demo_username = "demo"
        demo_password = "demo1234"
        user, created_user = User.objects.get_or_create(
            username=demo_username,
            defaults={"email": demo_email}
        )
        if created_user:
            user.set_password(demo_password)
            user.is_superuser = True
            user.is_staff = True
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Created superuser {demo_username} / {demo_password}"))
        else:
            self.stdout.write("Superuser 'demo' already exists")

        # Create or get Project
        project, created_project = Project.objects.get_or_create(
            slug="demo",
            defaults={"owner": user, "name": "Demo Project"}
        )
        if created_project:
            self.stdout.write(self.style.SUCCESS("Created Project with slug 'demo'"))
        else:
            # Ensure ownership if previously different
            if project.owner_id != user.id:
                project.owner = user
                project.save(update_fields=["owner"])
            self.stdout.write("Project 'demo' already exists")

        # Create or get WallConfig
        wc, created_wc = WallConfig.objects.get_or_create(project=project)
        if created_wc:
            self.stdout.write(self.style.SUCCESS("Created WallConfig for 'demo'"))

        # Create a sample approved testimonial
        if not project.testimonials.filter(status="approved").exists():
            Testimonial.objects.create(
                project=project,
                author_name="Jane Doe",
                content_text="This testimonial wall is awesome! Super quick to set up.",
                rating=5,
                media_type="text",
                status="approved",
                source="seed",
            )
            self.stdout.write(self.style.SUCCESS("Added an approved sample testimonial"))
        else:
            self.stdout.write("Approved testimonial already present")

        self.stdout.write(self.style.SUCCESS("Seed complete. Test at: /t/demo/wall and /t/demo/submit"))
