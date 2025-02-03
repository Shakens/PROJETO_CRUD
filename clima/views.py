from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.utils import timezone
from .models import TipoSensor, Sala, Parametro, LeituraTemperatura, Pavimento, SensorFisico, SensorLogico, Orientacao, Relatorio
from .forms import TipoSensorForm, SalaForm, ParametroForm, LeituraTemperaturaForm, PavimentoForm, SensorFisicoForm, SensorLogicoForm, OrientacaoForm, RelatorioForm

# ===================== API para atualização de dados =====================

def atualizar_dados(request):
    """
    Retorna os dados atualizados de temperatura e umidade no formato JSON
    para atualização automática do dashboard.
    """
    leituras = LeituraTemperatura.objects.order_by('-data_leitura')[:10]  # Últimas 10 leituras
    labels = [leitura.data_leitura.strftime("%d/%m %H:%M") for leitura in leituras]
    temperaturas = [leitura.temperatura for leitura in leituras]
    umidades = [leitura.umidade for leitura in leituras]

    total_sensores = TipoSensor.objects.count()
    total_salas = Sala.objects.count()

    return JsonResponse({
        "labels": labels,
        "temperaturas": temperaturas,
        "umidades": umidades,
        "total_sensores": total_sensores,
        "total_salas": total_salas,
    })

# ===================== API para dados de temperatura =====================

def temperatura_dados(request):
    """
    Retorna os últimos dados de temperatura no formato JSON.
    """
    leituras = LeituraTemperatura.objects.order_by('-data_leitura')[:10]
    dados = [{
        "data": leitura.data_leitura.strftime("%d/%m %H:%M"),
        "temperatura": leitura.temperatura,
        "umidade": leitura.umidade,
    } for leitura in leituras]
    return JsonResponse({"leituras": dados})

# ===================== Dashboard =====================

def dashboard_view(request):
    """
    Renderiza o dashboard exibindo totais e gráficos.
    """
    total_sensores = TipoSensor.objects.count()
    total_salas = Sala.objects.count()
    total_parametros = Parametro.objects.count()

    # Obtendo as últimas 10 leituras
    leituras = LeituraTemperatura.objects.order_by('-data_leitura')[:10]
    labels = [leitura.data_leitura.strftime("%d/%m %H:%M") for leitura in leituras]
    valores = [leitura.temperatura for leitura in leituras]

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
    template_name = "clima/Home/home.html"
    context_object_name = "tipo_sensores"

class TipoSensorListView(ListView):
    model = TipoSensor
    template_name = "clima/TipoSensor/tipo_sensor_list.html"
    context_object_name = "tipo_sensores"

class TipoSensorCreateView(CreateView):
    model = TipoSensor
    form_class = TipoSensorForm
    template_name = "clima/TipoSensor/tipo_sensor_form.html"
    success_url = reverse_lazy("tipo_sensor_list")

class TipoSensorUpdateView(UpdateView):
    model = TipoSensor
    form_class = TipoSensorForm
    template_name = "clima/TipoSensor/tipo_sensor_form.html"
    success_url = reverse_lazy("tipo_sensor_list")

class TipoSensorDetailView(DetailView):
    model = TipoSensor
    template_name = "clima/TipoSensor/tipo_sensor_detail.html"

class TipoSensorDeleteView(DeleteView):
    model = TipoSensor
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
    template_name = "clima/Sala/sala_form.html"
    success_url = reverse_lazy("sala_list")

class SalaUpdateView(UpdateView):
    model = Sala
    form_class = SalaForm
    template_name = "clima/Sala/sala_form.html"
    success_url = reverse_lazy("sala_list")

class SalaDetailView(DetailView):
    model = Sala
    template_name = "clima/Sala/sala_detail.html"

class SalaDeleteView(DeleteView):
    model = Sala
    template_name = "clima/Sala/sala_delete.html"
    success_url = reverse_lazy("sala_list")

# ===================== Views para Parâmetros =====================

class ParametroListView(ListView):
    model = Parametro
    template_name = "clima/Parametro/parametro_list.html"
    context_object_name = "parametros"

class ParametroCreateView(CreateView):
    model = Parametro
    form_class = ParametroForm
    template_name = "clima/Parametro/parametro_form.html"
    success_url = reverse_lazy("parametro_list")

class ParametroUpdateView(UpdateView):
    model = Parametro
    form_class = ParametroForm
    template_name = "clima/Parametro/parametro_form.html"
    success_url = reverse_lazy("parametro_list")

class ParametroDetailView(DetailView):
    model = Parametro
    template_name = "clima/Parametro/parametro_detail.html"

class ParametroDeleteView(DeleteView):
    model = Parametro
    template_name = "clima/Parametro/parametro_delete.html"
    success_url = reverse_lazy("parametro_list")

# ===================== Views para Leitura de Temperatura =====================

class LeituraTemperaturaCreateView(CreateView):
    model = LeituraTemperatura
    form_class = LeituraTemperaturaForm
    template_name = "clima/LeituraTemperatura/leitura_temperatura_form.html"
    success_url = reverse_lazy("leitura_temperatura_list")

class LeituraTemperaturaListView(ListView):
    model = LeituraTemperatura
    template_name = "clima/LeituraTemperatura/leitura_temperatura_list.html"
    context_object_name = "leituras_temperatura"

class LeituraTemperaturaDetailView(DetailView):
    model = LeituraTemperatura
    template_name = "clima/LeituraTemperatura/leitura_temperatura_detail.html"

# ===================== Views para Pavimentos =====================

class PavimentoListView(ListView):
    model = Pavimento
    template_name = "clima/Pavimento/pavimento_list.html"
    context_object_name = "pavimentos"

class PavimentoCreateView(CreateView):
    model = Pavimento
    form_class = PavimentoForm
    template_name = "clima/Pavimento/pavimento_form.html"
    success_url = reverse_lazy("pavimento_list")

class PavimentoUpdateView(UpdateView):
    model = Pavimento
    form_class = PavimentoForm
    template_name = "clima/Pavimento/pavimento_form.html"
    success_url = reverse_lazy("pavimento_list")

class PavimentoDetailView(DetailView):
    model = Pavimento
    template_name = "clima/Pavimento/pavimento_detail.html"

class PavimentoDeleteView(DeleteView):
    model = Pavimento
    template_name = "clima/Pavimento/pavimento_delete.html"
    success_url = reverse_lazy("pavimento_list")

# ===================== Views para Sensor Físico =====================

class SensorFisicoListView(ListView):
    model = SensorFisico
    template_name = 'clima/SensorFisico/sensor_fisico_list.html'
    context_object_name = 'sensores_fisicos'

class SensorFisicoCreateView(CreateView):
    model = SensorFisico
    form_class = SensorFisicoForm
    template_name = 'clima/SensorFisico/sensor_fisico_form.html'
    success_url = reverse_lazy('sensor_fisico_list')

class SensorFisicoUpdateView(UpdateView):
    model = SensorFisico
    form_class = SensorFisicoForm
    template_name = 'clima/SensorFisico/sensor_fisico_form.html'
    success_url = reverse_lazy('sensor_fisico_list')

class SensorFisicoDetailView(DetailView):
    model = SensorFisico
    template_name = 'clima/SensorFisico/sensor_fisico_detail.html'
    context_object_name = 'sensor_fisico'

class SensorFisicoDeleteView(DeleteView):
    model = SensorFisico
    template_name = 'clima/SensorFisico/sensor_fisico_confirm_delete.html'
    success_url = reverse_lazy('sensor_fisico_list')

# ===================== Views para Sensor Lógico =====================

class SensorLogicoListView(ListView):
    model = SensorLogico
    template_name = "clima/SensorLogico/sensor_logico_list.html"
    context_object_name = "sensor_logicos"

class SensorLogicoCreateView(CreateView):
    model = SensorLogico
    form_class = SensorLogicoForm
    template_name = "clima/SensorLogico/sensor_logico_form.html"
    success_url = reverse_lazy("sensor_logico_list")

class SensorLogicoUpdateView(UpdateView):
    model = SensorLogico
    form_class = SensorLogicoForm
    template_name = "clima/SensorLogico/sensor_logico_form.html"
    success_url = reverse_lazy("sensor_logico_list")

class SensorLogicoDetailView(DetailView):
    model = SensorLogico
    template_name = "clima/SensorLogico/sensor_logico_detail.html"
    context_object_name = "sensor_logico"

class SensorLogicoDeleteView(DeleteView):
    model = SensorLogico
    template_name = "clima/SensorLogico/sensor_logico_confirm_delete.html"
    success_url = reverse_lazy("sensor_logico_list")

# ===================== Views para Orientação =====================

class OrientacaoListView(ListView):
    model = Orientacao
    template_name = 'clima/Orientacao/orientacao_list.html'
    context_object_name = 'orientacoes'

class OrientacaoCreateView(CreateView):
    model = Orientacao
    form_class = OrientacaoForm
    template_name = 'clima/Orientacao/orientacao_form.html'
    success_url = reverse_lazy('orientacao_list')

class OrientacaoUpdateView(UpdateView):
    model = Orientacao
    form_class = OrientacaoForm
    template_name = 'clima/Orientacao/orientacao_form.html'
    success_url = reverse_lazy('orientacao_list')

class OrientacaoDetailView(DetailView):
    model = Orientacao
    template_name = 'clima/Orientacao/orientacao_detail.html'
    context_object_name = 'orientacao'

class OrientacaoDeleteView(DeleteView):
    model = Orientacao
    template_name = 'clima/Orientacao/orientacao_delete.html'
    success_url = reverse_lazy('orientacao_list')

# ===================== Views para Relatorio =====================

class RelatorioListView(ListView):
    model = Relatorio
    template_name = 'clima/Relatorio/relatorio_list.html'
    context_object_name = 'relatorios'

class RelatorioCreateView(CreateView):
    model = Relatorio
    form_class = RelatorioForm
    template_name = 'clima/Relatorio/relatorio_form.html'
    success_url = reverse_lazy('relatorio_list')

class RelatorioUpdateView(UpdateView):
    model = Relatorio
    form_class = RelatorioForm
    template_name = 'clima/Relatorio/relatorio_form.html'
    success_url = reverse_lazy('relatorio_list')

class RelatorioDetailView(DetailView):
    model = Relatorio
    template_name = 'clima/Relatorio/relatorio_detail.html'
    context_object_name = 'relatorio'

class RelatorioDeleteView(DeleteView):
    model = Relatorio
    template_name = 'clima/Relatorio/relatorio_delete.html'
    success_url = reverse_lazy('relatorio_list')