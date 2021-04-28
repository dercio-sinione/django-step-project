from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

from webapp.models import Actividades


class FormActividade(forms.ModelForm):
    # dataInicio = forms.DateInput()
    # dataTermino = forms.DateInput()
    class Meta:
        model = Actividades
        fields = ['titulo', 'subTitulo', 'objectivos', 'conteudo',
                  'localizacao', 'imagem', 'dataInicio', 'dataTermino']
        widgets = {
            'dataInicio': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'}),
            'dataTermino': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'}),
        }
