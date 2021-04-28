from django import forms

from webapp.models import Slides


class FormSlide(forms.ModelForm):
    class Meta:
        model = Slides
        fields = ['area', 'imagem']
