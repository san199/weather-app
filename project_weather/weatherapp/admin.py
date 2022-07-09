from django.contrib import admin
from weatherapp.models import Weather, WeatherType

from weatherapp.models import AppUser

# Register your models here.

class AppUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', \
            'email', 'contact', 'dob', 'password','address',\
                'created_at')

    list_filter = ('first_name','created_at')
    search_fields = ('first_name', 'last_name')

class WeatherTypeAdmin(admin.ModelAdmin):
    list_display = ('weather_type',)

class WeatherAdmin(admin.ModelAdmin):
    list_display = ('weather_type', 'user', 'description')

admin.site.register(AppUser, AppUserAdmin)
admin.site.register(WeatherType,WeatherTypeAdmin)
admin.site.register(Weather, WeatherAdmin)

admin.site.site_title = "Admin Dashboard"
admin.site.site_header = "MindRisers"
admin.site.index_title = "MindRisers Admin"
admin.site.app_index = "WAPP"
