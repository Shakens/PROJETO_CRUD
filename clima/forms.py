from django import forms
from .models import TipoSensor, Sala  # Alterado para Salas


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
        # Se precisar de validação adicional, adicione aqui
        return descricao

    def clean_limite_inferior_permitido(self):
        limite_inferior = self.cleaned_data.get("limite_inferior_permitido")
        if limite_inferior < 0:
            raise forms.ValidationError("O limite inferior permitido não pode ser negativo.")
        return limite_inferior


# Alterado para SalasForm
class SalaForm(forms.ModelForm):  # Certifique-se de que está no plural
    class Meta:
        model = Sala  # Corrigido para Salas
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
        # Adicione validações adicionais para o campo de localização, se necessário
        return localizacao
