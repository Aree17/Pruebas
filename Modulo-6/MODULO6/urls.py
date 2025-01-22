"""
URL configuration for MODULO6 project.

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
from Estadisticas import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('estadistica/', views.estadistica, name='estadistica'),
    path('estadisticas/meseros/', views.estadisticas_meseros, name='estadisticas_meseros'),
    path('estadisticas/mesas/', views.estadisticas_mesas, name='estadisticas_mesas'),
    path('estadisticas/productos/', views.estadisticas_productos, name='estadisticas_productos'),
]
