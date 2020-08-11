from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.createpage, name="create"),
    path("editpage/", views.editpage, name="editpage"),
    path("random/", views.randompage, name="random")
]