from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('pages.urls')),
    path('api/', include('core.api_urls')),
    path('accounts/', include('allauth.urls')),
    path('control/', admin.site.urls),
    path('users/', include('users.urls')),
    path('weather/', include('weather.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns