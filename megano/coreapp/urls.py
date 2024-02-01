from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page
app_name = 'coreapp'


urlpatterns = [
    path("base/", base_view, name="base"),
    path("about/", about_view, name="about"),
    path("index/", IndexView.as_view(), name="index"),
]
