from django.shortcuts import render
from django.db import models
from django.db.models import Q, Avg
from datetime import timedelta
from django.utils import timezone
from django.views import View
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from django.http import JsonResponse, HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.utils import timezone
from .models import TipoSensor, Sala, Parametro, Pavimento, SensorFisico, SensorLogico, Orientacao, LeituraSensor, Leitura
from .forms import TipoSensorForm, SalaForm, ParametroForm, PavimentoForm, SensorFisicoForm, SensorLogicoForm, OrientacaoForm

# ===================== Dashboard =====================
def dashboard_view(request):
    total_sensores = TipoSensor.objects.count()
    total_salas = Sala.objects.count()
    total_parametros = Parametro.objects.count()
    return render(request, 'clima/Dashboard/dashboard.html')

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
    context_object_name = "tipo_sensor"

class TipoSensorDeleteView(DeleteView):
    model = TipoSensor
    template_name = 'clima/TipoSensor/tipo_sensor_delete.html'
    success_url = reverse_lazy('tipo_sensor_list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        # Verifica se há Sensores Lógicos vinculados
        if SensorLogico.objects.filter(tipo=self.object).exists():
            messages.error(request, "❌ Este Tipo de Sensor não pode ser excluído porque está vinculado a um ou mais Sensores Lógicos.")
            return redirect('tipo_sensor_list')  # Redireciona de volta para a lista
        
        return super().post(request, *args, **kwargs)

# ===================== Views para Salas =====================
class SalaListView(ListView):
    model = Sala
    template_name = 'clima/Sala/sala_list.html'
    context_object_name = 'sala'

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
    template_name = 'clima/SensorFisico/sensor_fisico_delete.html'
    success_url = reverse_lazy('sensor_fisico_list')
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        # Verifica se o SensorFisico está vinculado a algum SensorLogico
        if SensorLogico.objects.filter(sensor_fisico=self.object).exists():
            messages.error(request, "❌ Este Sensor Físico não pode ser excluído porque está vinculado a um ou mais Sensores Lógicos.")
            return redirect('sensor_fisico_list')  # Redireciona para a lista de sensores

        # Se não houver SensorLogico vinculado, exclui o SensorFisico
        return super().post(request, *args, **kwargs)

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
    template_name = 'clima/SensorLogico/sensor_logico_detail.html'
    context_object_name = 'sensor_logico'


class SensorLogicoDeleteView(DeleteView):
    model = SensorLogico
    template_name = "clima/SensorLogico/sensor_logico_delete.html"
    success_url = reverse_lazy("sensor_logico_list")

# ===================== Views para Orientação =====================

class OrientacaoListView(ListView):
    model = Orientacao
    template_name = 'clima/Orientacao/orientacao_list.html'
    context_object_name = 'orientacoes'

    def get_queryset(self):
        return Orientacao.objects.all().order_by('id')


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
    context_object_name = 'orientacao'
    success_url = reverse_lazy('orientacao_list')

# ===================== Views para Relatórios =====================
def relatorio_list(request):
    # Obter os filtros da URL
    sala = request.GET.get('sala')
    tipo_sensor = request.GET.get('tipo_sensor')
    data_inicial = request.GET.get('data_inicial')
    data_final = request.GET.get('data_final')

    leituras = LeituraSensor.objects.all()

    if sala:
        leituras = leituras.filter(leitura__sala_id=sala)
    if tipo_sensor:
        leituras = leituras.filter(sensor_logico__tipo_sensor_id=tipo_sensor)
    if data_inicial:
        leituras = leituras.filter(leitura__data_hora__gte=data_inicial)
    if data_final:
        leituras = leituras.filter(leitura__data_hora__lte=data_final)

    return render(request, 'relatorio/relatorio_list.html', {'leituras': leituras})

class RelatorioFormView(View):
    def get(self, request, *args, **kwargs):
        # Recuperando os parâmetros da URL
        sala_id = request.GET.get('sala')
        tipo_sensor_id = request.GET.get('tipo_sensor')
        data_inicial = request.GET.get('data_inicial')
        data_final = request.GET.get('data_final')

        # Inicializando a consulta para as leituras
        leituras = LeituraSensor.objects.all()

        # Aplicando filtros conforme os parâmetros passados
        if sala_id:
            leituras = leituras.filter(leitura__sala_id=sala_id)
        if tipo_sensor_id:
            leituras = leituras.filter(sensor_logico__tipo_sensor_id=tipo_sensor_id)
        if data_inicial:
            leituras = leituras.filter(leitura__data_hora__gte=data_inicial)
        if data_final:
            leituras = leituras.filter(leitura__data_hora__lte=data_final)

        # Se necessário, recuperar objetos relacionados, como salas ou tipo de sensor
        salas = Sala.objects.all()
        tipos_sensores = TipoSensor.objects.all()

        # Passando os dados para o template
        context = {
            'leituras': leituras,
            'salas': salas,
            'tipos_sensores': tipos_sensores,
            'sala_id': sala_id,
            'tipo_sensor_id': tipo_sensor_id,
            'data_inicial': data_inicial,
            'data_final': data_final,
        }
        
        return render(request, 'relatorios/relatorio_list.html', context)
    
 #--------------
def gerar_relatorio_historico(sala_id, data_inicio, data_fim):
    return LeituraSensor.objects.filter(
        Q(leitura__sala_id=sala_id) &
        Q(leitura__data_hora__gte=data_inicio) &
        Q(leitura__data_hora__lte=data_fim)
    ).order_by('leitura__data_hora')
#---------------------------
def sensores_criticos():
    # Definir limites aceitáveis de temperatura/umidade, por exemplo:
    limite_min = 20.0
    limite_max = 25.0

    # Consultar os sensores cujos valores de leitura estão fora desses limites
    sensores_criticos = LeituraSensor.objects.filter(
        Q(valor__lt=limite_min) | Q(valor__gt=limite_max)
    ).values('sensor_logico').annotate(contagem=models.Count('id')).order_by('-contagem')

    return sensores_criticos
#----------------------------
def relatorio_temperatura_umidade_agrupada(intervalo_minutos):
    # Definir o intervalo de tempo
    tempo_agrupado = timezone.now() - timedelta(minutes=intervalo_minutos)

    # Consultar leituras agrupadas por intervalo de tempo
    relatorio = LeituraSensor.objects.filter(
        leitura__data_hora__gte=tempo_agrupado
    ).values('leitura__data_hora').annotate(
        media_valor=Avg('valor')
    ).order_by('leitura__data_hora')

    return relatorio

# ===================== Gerar Relatório em PDF =====================

def render_pdf(request):
    # Obter os filtros da URL
    sala = request.GET.get('sala')
    tipo_sensor = request.GET.get('tipo_sensor')
    data_inicial = request.GET.get('data_inicial')
    data_final = request.GET.get('data_final')

    leituras = LeituraSensor.objects.all()

    if sala:
        leituras = leituras.filter(leitura__sala_id=sala)
    if tipo_sensor:
        leituras = leituras.filter(sensor_logico__tipo_sensor_id=tipo_sensor)
    if data_inicial:
        leituras = leituras.filter(leitura__data_hora__gte=data_inicial)
    if data_final:
        leituras = leituras.filter(leitura__data_hora__lte=data_final)

    # Gerar o PDF com o canvas
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="relatorio.pdf"'

    p = canvas.Canvas(response)

    p.setFont("Helvetica", 12)

    # Adicionando título ao PDF
    p.drawString(250, 800, "Relatório de Leituras")

    # Definindo os headers
    p.drawString(50, 760, "ID")
    p.drawString(100, 760, "Sala")
    p.drawString(200, 760, "Sensor")
    p.drawString(300, 760, "Valor")
    p.drawString(400, 760, "Data e Hora")

    y_position = 740  # Começando logo abaixo dos cabeçalhos

    # Preenchendo os dados das leituras
    for leitura in leituras:
        p.drawString(50, y_position, str(leitura.id))
        p.drawString(100, y_position, leitura.leitura.sala.nome)
        p.drawString(200, y_position, leitura.sensor_logico.nome)
        p.drawString(300, y_position, str(leitura.valor))
        p.drawString(400, y_position, str(leitura.leitura.data_hora))
        y_position -= 20  # Diminuindo a posição Y para a próxima linha

    p.showPage()
    p.save()

    return response
