from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import WeatherAppUser


class WeatherUserAdmin(UserAdmin):

    list_display = ['email', 'is_admin']

    def is_admin(self, obj):
        return obj.is_admin


admin.site.register(WeatherAppUser, WeatherUserAdmin)