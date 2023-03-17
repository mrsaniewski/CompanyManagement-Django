from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path("view/<int:id>", views.view, name="view"),
    path("", views.home, name="view"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("<int:id>", views.view, name="view"),
    path("loyality/<int:id>", views.loyality, name="loyality"),
]