from django.urls import path
from django.views.generic.base import TemplateView

app_name = 'profile_app'

urlpatterns = [
    path('', TemplateView.as_view(template_name='profile_app/profile.html'), name='profile'),
    path('change_profile/', TemplateView.as_view(template_name='profile_app/change_profile.html'), name='change_profile'),
]

