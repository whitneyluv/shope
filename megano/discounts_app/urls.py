from django.urls import path
from megano.discounts_app.views import get_discount
app_name = 'discounts'


urlpatterns = [
    path("", get_discount, name="discount"),
]