from string import Template
from django.utils.safestring import mark_safe
from django import forms


class PictureWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None, **kwargs):
        html =  Template("""{% load static %} <img src="{% static 'assets/img/icons/upload.png' %}" alt="Upload"/>""")
        return mark_safe(html.substitute())