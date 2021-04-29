from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django import forms

from step.models import Projectos

class FormProjecto(forms.ModelForm):
    class Meta:
        model = Projectos
        fields = ['categoria', 'descricao', 'custos', 'dataEntrega', 'estado',
                  'progresso', 'entidade']
        
        widgets = {
            'dataEntrega': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'}),
        }


@login_required
def projectos(request):
    return render(request, 'step/projectos.html',)


@login_required
def addProjecto(request):
    if request.method == 'POST':
        # Formulario de registar Projectos
        form = FormProjecto(request.POST,)
        # form = FormProjecto(request.POST, request.FILES,)
        form.instance.user = request.user

        # Validar o formulario
        if form.is_valid():
            form.save()
            titulo = form.cleaned_data.get('titulo')
            messages.success(
                request, f'Projecto "{titulo}" criado com sucesso!')
            return redirect('users:listarprojectos')
        else:
            messages.error(
                request, f'{form.errors}', extra_tags='danger')
    else:
        form = FormProjecto()
    return render(request, 'step/addprojectos.html', {'form': form})


# @login_required
# def changeProjecto(request, pk):
#     obj = get_object_or_404(Projectos, pk=pk)
#     if request.method == 'POST':
#         form = FormProjecto(request.POST, request.FILES, instance=obj)
#         form.instance.criadoPor = request.user

#         # Validar o formulario
#         if form.is_valid():
#             form.save()
#             titulo = form.cleaned_data.get('titulo')

#             messages.success(
#                 request, f'Projecto "{titulo}" alterado com sucesso!')
#             return redirect('users:listarprojectos')
#         else:
#             messages.error(
#                 request, f'{form.errors}', extra_tags='danger')
#     else:
#         form = FormProjecto(instance=obj)
#     return render(request, 'users/editarProjecto.html', {'form': form})
