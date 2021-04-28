from django import forms

from webapp.models import Sobre


class FormSobre(forms.ModelForm):
    class Meta:
        model = Sobre
        fields = ['titulo', 'conteudo']
