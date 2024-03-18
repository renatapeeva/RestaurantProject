"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from restaurant.views import index, rest1, rest2, rest3, rest4
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservations/', index, name='reservations'),
    path('rest1', rest1, name='rest1'),
    path('rest2', rest2, name='rest2'),
    path('rest3', rest3, name='rest3'),
    path('rest4', rest4, name='rest4'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
