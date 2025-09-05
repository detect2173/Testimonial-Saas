from django.urls import path
from . import views

urlpatterns = [
    path("t/<slug:slug>/submit", views.submit_testimonial, name="submit_testimonial"),
    path("t/<slug:slug>/wall", views.public_wall, name="public_wall"),
    path("embed/<slug:slug>.js", views.embed_script, name="embed_script"),
    path("healthz", views.healthz, name="healthz"),
]
