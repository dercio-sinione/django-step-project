from django import forms

from webapp.models import Projectos


class FormProjecto(forms.ModelForm):
    class Meta:
        model = Projectos
        fields = ['titulo', 'subTitulo', 'objectivos', 'conteudo', 'metas',
                  'imagem', 'dataInicio', 'dataTermino']
        widgets = {
            'dataInicio': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'}),
            'dataTermino': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'}),
        }
