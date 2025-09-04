from django.contrib import admin
from .models import Project, WallConfig, Testimonial

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name","owner","slug")

@admin.register(WallConfig)
class WallConfigAdmin(admin.ModelAdmin):
    list_display = ("project","theme","layout","max_items")

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("project","author_name","media_type","status","created_at")
    list_filter = ("status","media_type","project")
    search_fields = ("author_name","content_text")