from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = 'avatar', 'phone'
    list_display = 'pk', 'avatar', 'user', 'user_username', 'phone'

    ordering = ('pk',)

    def user_username(self, obj):
        return obj.user.username
