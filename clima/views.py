from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from .models import TipoSensor
from .forms import TipoSensorForm

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

class HomeListView(ListView):
    model = TipoSensor
    fields = ["nome", "descricao"]
    context_object_name = "tipo_sensores" 
    template_name = "clima/Home/home.html"

class TipoSensorListView(ListView):
    model = TipoSensor
    fields = ["nome", "descricao"]
    context_object_name = "tipo_sensores" 
    template_name = "clima/TipoSensor/tipo_sensor_list.html"


class TipoSensorCreateView(CreateView):
    model = TipoSensor
    form_class = TipoSensorForm  # Usa o ModelForm criado
    #fields = ["tipo", "descricao"]
    context_object_name = "tipo_sensor" 
    template_name = "clima/TipoSensor/tipo_sensor_form.html"
    success_url = reverse_lazy("tipo_sensor_list")


class TipoSensorUptadeView(UpdateView):
    model = TipoSensor
    form_class = TipoSensorForm  # Usa o ModelForm criado
    context_object_name = "tipo_sensor"
    template_name = "clima/TipoSensor/tipo_sensor_form.html"
    success_url = reverse_lazy("tipo_sensor_list")

class TipoSensorDetailView(DetailView):
    model = TipoSensor
    context_object_name = "tipo_sensor"
    template_name = "clima/TipoSensor/tipo_sensor_detail.html"
    fields = ["tipo", "descricao"]

class TipoSensorDeleteView(DeleteView):
    model = TipoSensor
    context_object_name = "tipo_sensor"
    template_name = "clima/TipoSensor/tipo_sensor_delete.html"
    success_url = reverse_lazy("tipo_sensor_list")


