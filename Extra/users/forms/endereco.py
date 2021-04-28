from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

from webapp.models import Endereco


class FormEndereco(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['localizacao', 'email', 'tel1', 'tel2']
