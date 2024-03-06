from django.urls import path
from megano.coreapp.views.about_view import about_view
from megano.coreapp.views.base_view import base_view
from megano.coreapp.views.index_view import IndexView

app_name = 'coreapp'


urlpatterns = [
    path("base/", base_view, name="base"),
    path("about/", about_view, name="about"),
    path("", IndexView.as_view(), name="index"),
]
