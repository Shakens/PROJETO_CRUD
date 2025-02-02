from django.shortcuts import render
from django.urls import reverse_lazy
from .models import TipoSensor, Sala  # Certifique-se de que o modelo correto é "Sala"
from .forms import TipoSensorForm, SalaForm  # Certifique-se de que o nome do formulário está correto
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

# ===================== Função para retornar dados de temperatura =====================
def temperatura_dados(request):
    return HttpResponse("Dados de temperatura")

# ===================== Views para Sensores =====================

class HomeListView(ListView):
    model = TipoSensor
    context_object_name = "tipo_sensores"
    template_name = "clima/Home/home.html"

class TipoSensorListView(ListView):
    model = TipoSensor
    context_object_name = "tipo_sensores"
    template_name = "clima/TipoSensor/tipo_sensor_list.html"

class TipoSensorCreateView(CreateView):
    model = TipoSensor
    form_class = TipoSensorForm
    context_object_name = "tipo_sensor"
    template_name = "clima/TipoSensor/tipo_sensor_form.html"
    success_url = reverse_lazy("tipo_sensor_list")

class TipoSensorUpdateView(UpdateView):
    model = TipoSensor
    form_class = TipoSensorForm
    context_object_name = "tipo_sensor"
    template_name = "clima/TipoSensor/tipo_sensor_form.html"
    success_url = reverse_lazy("tipo_sensor_list")

class TipoSensorDetailView(DetailView):
    model = TipoSensor
    context_object_name = "tipo_sensor"
    template_name = "clima/TipoSensor/tipo_sensor_detail.html"

class TipoSensorDeleteView(DeleteView):
    model = TipoSensor
    context_object_name = "tipo_sensor"
    template_name = "clima/TipoSensor/tipo_sensor_delete.html"
    success_url = reverse_lazy("tipo_sensor_list")

# ===================== View do Dashboard =====================

def dashboard_view(request):
    context = {
        'title': 'Dashboard',
        'total_sensores': TipoSensor.objects.count(),
        'total_salas': Sala.objects.count(),  # Total de salas, se desejar incluir no dashboard
    }
    return render(request, 'clima/Dashboard/dashboard.html', context)

# ===================== Views para Salas =====================

class SalaListView(ListView):
    model = Sala
    template_name = 'clima/Sala/sala_list.html'
    context_object_name = 'salas'  # Corrigido de 'sala' para 'salas', pois será uma lista

class SalaCreateView(CreateView):
    model = Sala
    form_class = SalaForm
    context_object_name = "sala"
    template_name = "clima/Sala/sala_form.html"
    success_url = reverse_lazy("sala_list")

class SalaUpdateView(UpdateView):
    model = Sala
    form_class = SalaForm
    context_object_name = "sala"
    template_name = "clima/Sala/sala_form.html"
    success_url = reverse_lazy("sala_list")

class SalaDetailView(DetailView):
    model = Sala
    context_object_name = "sala"
    template_name = "clima/Sala/sala_detail.html"

class SalaDeleteView(DeleteView):
    model = Sala
    context_object_name = "sala"
    template_name = "clima/Sala/sala_delete.html"
    success_url = reverse_lazy("sala_list")

