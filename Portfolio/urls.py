from django.contrib import admin
from django.urls import path
from app.views import home, contact, services, skills, projects, about, view_contact

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="name"),
    path("contact/", contact, name="contact"),
    path("services/", services, name="services"),
    path("skills/", skills, name="skills"),
    path("projects/", projects, name="projects"),
    path("about/", about, name="about"),
    path("view_contact/", view_contact, name="view_contact"),
]
