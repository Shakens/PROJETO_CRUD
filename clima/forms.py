from django import forms
from django.utils import timezone
from .models import TipoSensor, Sala, Parametro, LeituraSensor, Pavimento, SensorFisico, SensorLogico, Orientacao, Leitura  # Incluindo Orientacao

# Formulário para TipoSensor
class TipoSensorForm(forms.ModelForm):
    class Meta:
        model = TipoSensor
        fields = ['descricao', 'limite_inferior_permitido', 'limite_superior_permitido', 'unidade']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3, 'cols': 50}),
            'limite_inferior_permitido': forms.NumberInput(attrs={'step': '0.01'}),
            'limite_superior_permitido': forms.NumberInput(attrs={'step': '0.01'}),
        }

    def clean_descricao(self):
        descricao = self.cleaned_data.get("descricao")
        return descricao

    def clean_limite_inferior_permitido(self):
        limite_inferior = self.cleaned_data.get("limite_inferior_permitido")
        if limite_inferior < 0:
            raise forms.ValidationError("O limite inferior permitido não pode ser negativo.")
        return limite_inferior

    def clean_limite_superior_permitido(self):
        limite_superior = self.cleaned_data.get("limite_superior_permitido")
        if limite_superior < 0:
            raise forms.ValidationError("O limite superior permitido não pode ser negativo.")
        return limite_superior


# Formulário para Sala
class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['nome', 'sigla', 'id_pavimento', 'id_orientacao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'sigla': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if 'inválido' in nome.lower():
            raise forms.ValidationError("O nome da sala não pode conter a palavra 'inválido'.")
        return nome


# Formulário para Parametro
class ParametroForm(forms.ModelForm):
    class Meta:
        model = Parametro
        fields = '__all__'


# Formulário para Pavimento
class PavimentoForm(forms.ModelForm):
    class Meta:
        model = Pavimento
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if 'inválido' in nome.lower():
            raise forms.ValidationError("O nome do pavimento não pode conter a palavra 'inválido'.")
        return nome


# Formulário para SensorFisico
class SensorFisicoForm(forms.ModelForm):
    class Meta:
        model = SensorFisico
        fields = ['nome', 'sigla', 'descricao', 'tensao_min', 'tensao_max']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3, 'cols': 50}),
            'tensao_min': forms.NumberInput(attrs={'step': '0.01'}),
            'tensao_max': forms.NumberInput(attrs={'step': '0.01'}),
        }

    def clean_descricao(self):
        descricao = self.cleaned_data.get('descricao')
        return descricao

    def clean_tensao_min(self):
        tensao_min = self.cleaned_data.get('tensao_min')
        if tensao_min < 0:
            raise forms.ValidationError("A tensão mínima não pode ser negativa.")
        return tensao_min

    def clean_tensao_max(self):
        tensao_max = self.cleaned_data.get('tensao_max')
        if tensao_max < 0:
            raise forms.ValidationError("A tensão máxima não pode ser negativa.")
        return tensao_max


# Formulário para SensorLogico
class SensorLogicoForm(forms.ModelForm):
    class Meta:
        model = SensorLogico
        fields = ['sensor_fisico', 'tipo', 'descricao']
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_descricao(self):
        descricao = self.cleaned_data.get('descricao')
        if 'inválido' in descricao.lower():
            raise forms.ValidationError("A descrição não pode conter a palavra 'inválido'.")
        return descricao


# Formulário para Orientacao
class OrientacaoForm(forms.ModelForm):
    class Meta:
        model = Orientacao
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if "inválido" in nome.lower():
            raise forms.ValidationError("O nome da orientação não pode conter a palavra 'inválido'.")
        return nome

# Formulário para LeituraSensor
class LeituraSensorForm(forms.ModelForm):
    class Meta:
        model = LeituraSensor
        fields = ['sensor_logico', 'leitura', 'valor']
        widgets = {
            'sensor_logico': forms.Select(attrs={'class': 'form-control'}),
            'leitura': forms.Select(attrs={'class': 'form-control'}),  # Mudança de NumberInput para Select
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
        }


# Formulário para Leitura
class LeituraForm(forms.ModelForm):
    class Meta:
        model = Leitura
        fields = ['sala', 'data_hora']
        widgets = {
            'data_hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean_data_hora(self):
        data_hora = self.cleaned_data.get('data_hora')
        if data_hora > timezone.now():
            raise forms.ValidationError("A data e hora não podem ser no futuro.")
        return data_hora
