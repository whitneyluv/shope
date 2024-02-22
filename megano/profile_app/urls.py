from django.urls import path
from django.views.generic.base import TemplateView
from .views import ProfileView, ChangeProfileView

app_name = 'profile_app'

urlpatterns = [
    path('<pk>/', ProfileView.as_view(), name='profile'),
    path('<pk>/change_profile/', ChangeProfileView.as_view(), name='change_profile'),
]

