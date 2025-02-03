from django import forms
from django.utils import timezone
from .models import TipoSensor, Sala, Parametro, LeituraTemperatura, Pavimento, SensorFisico, SensorLogico, Orientacao, Relatorio  # Incluindo Orientacao

# Formulário para TipoSensor
class TipoSensorForm(forms.ModelForm):
    class Meta:
        model = TipoSensor
        fields = ["nome", "sigla", "descricao", "limite_inferior_permitido"]
        widgets = {
            "descricao": forms.Textarea(attrs={"rows": 3, "cols": 50}),
            "limite_inferior_permitido": forms.NumberInput(attrs={"step": "0.01"}),  # Campo numérico com precisão decimal
        }

    def clean_nome(self):
        nome = self.cleaned_data.get("nome")
        if "inválido" in nome.lower():
            raise forms.ValidationError("O tipo de sensor não pode conter a palavra 'inválido'.")
        return nome

    def clean_descricao(self):
        descricao = self.cleaned_data.get("descricao")
        return descricao

    def clean_limite_inferior_permitido(self):
        limite_inferior = self.cleaned_data.get("limite_inferior_permitido")
        if limite_inferior < 0:
            raise forms.ValidationError("O limite inferior permitido não pode ser negativo.")
        return limite_inferior


# Formulário para Sala
class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala  # Modelo Sala
        fields = ['nome', 'descricao', 'capacidade', 'localizacao']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3, 'cols': 50}),
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if 'inválido' in nome.lower():
            raise forms.ValidationError("O nome da sala não pode conter a palavra 'inválido'.")
        return nome

    def clean_capacidade(self):
        capacidade = self.cleaned_data.get('capacidade')
        if capacidade < 0:
            raise forms.ValidationError("A capacidade não pode ser negativa.")
        return capacidade

    def clean_localizacao(self):
        localizacao = self.cleaned_data.get('localizacao')
        return localizacao


# Formulário para Parametro
class ParametroForm(forms.ModelForm):
    class Meta:
        model = Parametro
        fields = '__all__'


# Formulário para Leitura de Temperatura
class LeituraTemperaturaForm(forms.ModelForm):
    class Meta:
        model = LeituraTemperatura  # Modelo para leitura de temperatura
        fields = ['sensor', 'temperatura', 'data_leitura']  # Adapte conforme necessário
        widgets = {
            'data_leitura': forms.DateTimeInput(attrs={'type': 'datetime-local'}),  # Formato de data e hora
            'temperatura': forms.NumberInput(attrs={'step': '0.01'}),  # Temperatura com casas decimais
        }

    def clean_temperatura(self):
        temperatura = self.cleaned_data.get('temperatura')
        if temperatura < -50 or temperatura > 100:
            raise forms.ValidationError("A temperatura deve estar entre -50°C e 100°C.")
        return temperatura

    def clean_data_leitura(self):
        data_leitura = self.cleaned_data.get('data_leitura')
        if data_leitura > timezone.now():
            raise forms.ValidationError("A data de leitura não pode ser no futuro.")
        return data_leitura


# Formulário para Pavimento
class PavimentoForm(forms.ModelForm):
    class Meta:
        model = Pavimento
        fields = ['nome', 'descricao', 'andar', 'localizacao']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3, 'cols': 50}),
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if 'inválido' in nome.lower():
            raise forms.ValidationError("O nome do pavimento não pode conter a palavra 'inválido'.")
        return nome

    def clean_andar(self):
        andar = self.cleaned_data.get('andar')
        if andar < 0:
            raise forms.ValidationError("O andar não pode ser negativo.")
        return andar

    def clean_localizacao(self):
        localizacao = self.cleaned_data.get('localizacao')
        return localizacao


# Formulário para SensorFisico
class SensorFisicoForm(forms.ModelForm):
    class Meta:
        model = SensorFisico
        fields = ['tipo_sensor', 'sala', 'pavimento', 'localizacao', 'data_instalacao', 'ativo']
        widgets = {
            'data_instalacao': forms.DateInput(attrs={'type': 'date'}),  # Campo de data
        }

    def clean_localizacao(self):
        localizacao = self.cleaned_data.get('localizacao')
        if "inválido" in localizacao.lower():
            raise forms.ValidationError("A localização não pode conter a palavra 'inválido'.")
        return localizacao

    def clean_data_instalacao(self):
        data_instalacao = self.cleaned_data.get('data_instalacao')
        if data_instalacao > timezone.now().date():
            raise forms.ValidationError("A data de instalação não pode ser no futuro.")
        return data_instalacao


# Formulário para SensorLogico
class SensorLogicoForm(forms.ModelForm):
    class Meta:
        model = SensorLogico
        fields = ['tipo_sensor', 'sensor_fisico', 'descricao', 'ativo', 'data_instalacao']
        widgets = {
            'data_instalacao': forms.DateInput(attrs={'type': 'date'}),  # Campo de data
        }

    def clean_descricao(self):
        descricao = self.cleaned_data.get('descricao')
        if "inválido" in descricao.lower():
            raise forms.ValidationError("A descrição não pode conter a palavra 'inválido'.")
        return descricao

    def clean_data_instalacao(self):
        data_instalacao = self.cleaned_data.get('data_instalacao')
        if data_instalacao > timezone.now().date():
            raise forms.ValidationError("A data de instalação não pode ser no futuro.")
        return data_instalacao


# Formulário para Orientacao
class OrientacaoForm(forms.ModelForm):
    class Meta:
        model = Orientacao
        fields = ['nome', 'descricao']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if "inválido" in nome.lower():
            raise forms.ValidationError("O nome da orientação não pode conter a palavra 'inválido'.")
        return nome

# Formulário para Relatorio
class RelatorioForm(forms.Form):
    nome_relatorio = forms.CharField(max_length=100)
    descricao = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 50}))
    data_inicio = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    data_fim = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    def clean_nome_relatorio(self):
        nome_relatorio = self.cleaned_data.get('nome_relatorio')
        if 'inválido' in nome_relatorio.lower():
            raise forms.ValidationError("O nome do relatório não pode conter a palavra 'inválido'.")
        return nome_relatorio

    def clean_data_inicio(self):
        data_inicio = self.cleaned_data.get('data_inicio')
        if data_inicio > timezone.now():
            raise forms.ValidationError("A data de início não pode ser no futuro.")
        return data_inicio

    def clean_data_fim(self):
        data_fim = self.cleaned_data.get('data_fim')
        if data_fim > timezone.now():
            raise forms.ValidationError("A data de fim não pode ser no futuro.")
        return data_fim
