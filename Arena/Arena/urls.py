"""
URL configuration for Arena project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from Home import views as home_views
from Volei import views as volei_views
from Matricula import views as matricula_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.Home, name='Home'),
    path('Volei/', volei_views.Volei, name='Volei'),
    path('Matricula/', matricula_views.Matricula, name='Matricula'),
]
