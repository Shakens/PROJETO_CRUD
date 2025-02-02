from django.shortcuts import render
from django.urls import reverse_lazy
from .models import TipoSensor, Sala, Parametro, LeituraTemperatura, Pavimento  # Incluindo Pavimento
from .forms import TipoSensorForm, SalaForm, ParametroForm, LeituraTemperaturaForm, PavimentoForm
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.utils import timezone

# ===================== Funções para dados de temperatura =====================

def temperatura_dados(request):
    """
    Função para retornar os dados de temperatura no formato JSON
    com base no parâmetro de filtro (semana ou mês).
    """
    periodo = request.GET.get('periodo', 'semana')  # Captura o parâmetro 'periodo' da URL
    
    # Exemplo de dados reais: podemos consultar a tabela LeituraTemperatura aqui
    # Filtrando pelas últimas leituras de temperatura (exemplo)
    if periodo == 'semana':
        dados = LeituraTemperatura.objects.filter(data_leitura__gte='2025-01-29')  # Exemplo de filtro por data
    elif periodo == 'mes':
        dados = LeituraTemperatura.objects.filter(data_leitura__gte='2025-01-01')

    # Preparando dados simulados ou reais
    labels = [str(leitura.data_leitura.date()) for leitura in dados]  # Datas das leituras
    valores = [leitura.temperatura for leitura in dados]  # Temperaturas das leituras
    
    return JsonResponse({'labels': labels, 'valores': valores})

# ===================== Views para o Dashboard =====================

def dashboard_view(request):
    """
    Função para o Dashboard, exibindo o total de sensores, salas e parâmetros,
    além de gerar dados para o gráfico de temperatura.
    """
    # Consultando os totais
    total_sensores = TipoSensor.objects.count()
    total_salas = Sala.objects.count()
    total_parametros = Parametro.objects.count()
    
    # Obter dados de temperatura simulados ou reais
    # No caso real, aqui seria uma consulta ao modelo de leituras de temperatura
    labels = ["2025-01-29", "2025-01-30", "2025-01-31"]
    valores = [23, 24, 25]  # Simulando valores de temperatura para o gráfico

    context = {
        'title': 'Dashboard',
        'total_sensores': total_sensores,
        'total_salas': total_salas,
        'total_parametros': total_parametros,
        'labels': labels,
        'valores': valores,
    }

    return render(request, 'clima/Dashboard/dashboard.html', context)

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

# ===================== Views para Salas =====================

class SalaListView(ListView):
    model = Sala
    template_name = 'clima/Sala/sala_list.html'
    context_object_name = 'salas'

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

# ===================== Views para Parâmetros =====================

class ParametroListView(ListView):
    model = Parametro
    context_object_name = "parametros"
    template_name = "clima/Parametro/parametro_list.html"

class ParametroCreateView(CreateView):
    model = Parametro
    form_class = ParametroForm
    context_object_name = "parametro"
    template_name = "clima/Parametro/parametro_form.html"
    success_url = reverse_lazy("parametro_list")

class ParametroUpdateView(UpdateView):
    model = Parametro
    form_class = ParametroForm
    context_object_name = "parametro"
    template_name = "clima/Parametro/parametro_form.html"
    success_url = reverse_lazy("parametro_list")

class ParametroDetailView(DetailView):
    model = Parametro
    context_object_name = "parametro"
    template_name = "clima/Parametro/parametro_detail.html"

class ParametroDeleteView(DeleteView):
    model = Parametro
    context_object_name = "parametro"
    template_name = "clima/Parametro/parametro_delete.html"
    success_url = reverse_lazy("parametro_list")

# ===================== Views para Leitura de Temperatura =====================

class LeituraTemperaturaCreateView(CreateView):
    model = LeituraTemperatura
    form_class = LeituraTemperaturaForm
    context_object_name = "leitura_temperatura"
    template_name = "clima/LeituraTemperatura/leitura_temperatura_form.html"
    success_url = reverse_lazy("leitura_temperatura_list")

class LeituraTemperaturaListView(ListView):
    model = LeituraTemperatura
    context_object_name = "leituras_temperatura"
    template_name = "clima/LeituraTemperatura/leitura_temperatura_list.html"

class LeituraTemperaturaDetailView(DetailView):
    model = LeituraTemperatura
    context_object_name = "leitura_temperatura"
    template_name = "clima/LeituraTemperatura/leitura_temperatura_detail.html"

# ===================== Views para Pavimentos =====================

class PavimentoListView(ListView):
    model = Pavimento
    context_object_name = "pavimentos"
    template_name = "clima/Pavimento/pavimento_list.html"

class PavimentoCreateView(CreateView):
    model = Pavimento
    form_class = PavimentoForm
    context_object_name = "pavimento"
    template_name = "clima/Pavimento/pavimento_form.html"
    success_url = reverse_lazy("pavimento_list")

class PavimentoUpdateView(UpdateView):
    model = Pavimento
    form_class = PavimentoForm
    context_object_name = "pavimento"
    template_name = "clima/Pavimento/pavimento_form.html"
    success_url = reverse_lazy("pavimento_list")

class PavimentoDetailView(DetailView):
    model = Pavimento
    context_object_name = "pavimento"
    template_name = "clima/Pavimento/pavimento_detail.html"

class PavimentoDeleteView(DeleteView):
    model = Pavimento
    context_object_name = "pavimento"
    template_name = "clima/Pavimento/pavimento_delete.html"
    success_url = reverse_lazy("pavimento_list")
