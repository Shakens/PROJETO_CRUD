from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from django.http import JsonResponse, HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.utils import timezone
from .models import TipoSensor, Sala, Parametro, Pavimento, SensorFisico, SensorLogico, Orientacao, Relatorio, LeituraSensor, Leitura
from .forms import TipoSensorForm, SalaForm, ParametroForm, PavimentoForm, SensorFisicoForm, SensorLogicoForm, OrientacaoForm, LeituraSensorForm, RelatorioForm, LeituraForm

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
    template_name = "clima/TipoSensor/tipo_sensor_delete.html"
    success_url = reverse_lazy("tipo_sensor_list")

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

# ===================== Views para Leitura Sensor =====================
class LeituraSensorListView(ListView):
    model = LeituraSensor
    template_name = 'leitura_sensor/leitura_sensor_list.html'
    context_object_name = 'leituras_sensores'

class LeituraSensorCreateView(CreateView):
    model = LeituraSensor
    form_class = LeituraSensorForm
    template_name = 'leitura_sensor/form.html'
    success_url = reverse_lazy('listar_leitura_sensor')

    def form_valid(self, form):
        return super().form_valid(form)

# ===================== Views para Leitura =====================
class LeituraCreateView(CreateView):
    model = Leitura
    form_class = LeituraForm
    template_name = 'clima/Leitura/leitura_form.html'
    success_url = reverse_lazy('leitura_list')

    def form_valid(self, form):
        sala_id = self.kwargs['sala_id']
        sala = get_object_or_404(Sala, id=sala_id)
        form.instance.sala = sala
        form.instance.data_hora = timezone.now()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('listar_leitura')

# ===================== Gerar Relatório em PDF =====================
def gerar_relatorio(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio_leituras.pdf"'
    p = canvas.Canvas(response, pagesize=letter)
    p.setFont("Helvetica", 12)
    p.drawString(100, 750, "Relatório de Leituras")
    leituras = Leitura.objects.all()
    y_position = 730
    for leitura in leituras:
        p.drawString(100, y_position, f"Data: {leitura.data_hora} | Valor: {leitura.valor}")
        y_position -= 20
    p.showPage()
    p.save()
    return response
