"""
URL configuration for setup project.

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

from clima.views import (
    HomeListView,
    TipoSensorCreateView,
    TipoSensorDeleteView,
    TipoSensorDetailView,
    TipoSensorListView,
    TipoSensorUptadeView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",   HomeListView.as_view(), name="home"),
    path("sensor/",   TipoSensorListView.as_view(), name="tipo_sensor_list"),
    path("sensor/create", TipoSensorCreateView.as_view(), name="tipo_sensor_create"),
    path("sensor/update/<int:pk>", TipoSensorUptadeView.as_view(), name="tipo_sensor_update"),
    path("sensor/delete/<int:pk>", TipoSensorDeleteView.as_view(), name="tipo_sensor_delete"),
    path("sensor/detail/<int:pk>", TipoSensorDetailView.as_view(), name="tipo_sensor_detail"),
]
