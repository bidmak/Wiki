from django.urls import path

from . import views



app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:TITLE>", views.entry_page, name="TITLE"),
    path("add", views.new_page, name="add"),
    path("edit", views.edit, name="edit"),
    path("random", views.random, name="random")
]
