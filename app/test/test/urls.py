from django.contrib import admin
from django.urls import path, include
from .celeryapp import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('celeryapp/', include(urls.urls)),
]
