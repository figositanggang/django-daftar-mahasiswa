from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "mahasiswa"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("edit/<int:nim>/", views.edit, name="edit"),
    path("delete/<int:nim>/", views.delete, name="delete"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
