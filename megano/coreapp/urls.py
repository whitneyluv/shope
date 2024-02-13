from django.urls import path
from django.views.generic import TemplateView

app_name = 'coreapp'

urlpatterns = [
    path('core/', TemplateView.as_view(template_name='coreapp/base.html'), name='core'),
    path('index/', TemplateView.as_view(template_name='coreapp/index.html'), name='core'),
]
