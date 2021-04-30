from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from step.models import Perfil


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


def registar(request):
    """
    Registar Usuário.
    """
    if request.method=='POST':
        # Formulario de registar usuario
        form = UserRegisterForm(request.POST)
        # Validar o formulario de registar usuario
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get('username')
            messages.success(request,f'A sua conta foi criada, agora podes fazer o login.')
            return redirect('step:login')
    else:
        form = UserRegisterForm()
    
    return render(request,'step/registar.html',{'form':form})
