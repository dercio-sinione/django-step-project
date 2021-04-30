from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django import forms

from step.models import Entidades, Projectos, Categorias

class FormProjecto(forms.ModelForm):
    class Meta:
        model = Projectos
        fields = ['categoria', 'descricao', 'custos', 'dataEntrega', 'estado',
                  'progresso', 'projecto']

        widgets = {
            'dataEntrega': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'}),
        }

@login_required
def projectos(request):
    context = {
        'projectos': Projectos.objects.all()
        }
    return render(request, 'step/projectos.html', context)


@login_required
def addProjecto(request):
    entidade = None
    if request.method== 'GET':
        entidade = Entidades.objects.get(pk=request.GET['en'])
        
    form = FormProjecto()
    form.instance.entidade = entidade
    

    if request.method == 'POST':
        # Formulario de registar Projectos
        form = FormProjecto(request.POST, request.FILES,)
        # files = request.FILES['file_field']
        # form.instance.projecto = files
        # print(request.FILES['file_field'])
        # form = FormProjecto(request.POST, request.FILES,)
        form.instance.user = request.user
        entidade = Entidades.objects.get(pk=request.POST['idEntidade'])
        form.instance.entidade = entidade
        
        # Validar o formulario
        if form.is_valid():
            form.save()
            descricao = form.cleaned_data.get('descricao')
            messages.success(
                request, f'Projecto "{descricao}" criado com sucesso!')
            return redirect('step:projectos')
        else:
            messages.error(
                request, f'{form.errors}', extra_tags='danger')

    context = {'form': form, 'entidade': entidade}
    return render(request, 'step/addprojectos.html', context)


# @login_required
# def editarProjecto(request, pk):
#     obj = get_object_or_404(Projectos, pk=pk)
        
#     form = FormProjecto(instance=obj)
#     form.instance.entidade = obj.entidade
    

#     if request.method == 'POST':
#         form = FormProjecto(request.POST, request.FILES, instance=obj)
#         form.instance.user = request.user
#         form.instance.entidade = obj.entidade
        
#         file = request.FILES.get('projecto')
#         if file:
#             form.instance.projecto = file
#         else:
#             form.instance.projecto = obj.projecto
            
#         # Validar o formulario
#         if form.is_valid():
#             form.save()
#             descricao = form.cleaned_data.get('descricao')
#             messages.success(
#                 request, f'Projecto "{descricao}" criado com sucesso!')
#             return redirect('step:projectos')
#         else:
#             messages.error(
#                 request, f'{form.errors}', extra_tags='danger')

#     context = {'form': form, 'entidade': obj.entidade}
#     return render(request, 'step/editarprojectos.html', context)


@login_required
def editarProjecto(request, pk):
    
    print('----------------')
    obj = get_object_or_404(Projectos, pk=pk)
    if request.method == 'POST':
        print('----------------')
        print('----------------')
        print('----------------')
        obj = get_object_or_404(Projectos, pk=pk)
        form = FormProjecto(request.POST, request.FILES, instance=obj)
        form.instance.pk = obj.pk
        form.instance.user = obj.user
        form.instance.entidade = obj.entidade
                        
        # file = request.FILES.get('projecto')
        # if file:
        #     form.instance.projecto = file
        # else:
        #     form.instance.projecto = obj.projecto
        

        # Validar o formulario
        if form.is_valid():
            print('**********')
            print(form.instance.projecto)
            print(obj.projecto)
            print('**********')
            # form.save()
            descricao = form.cleaned_data.get('descricao')
            messages.success(
                request, f'Projecto "{descricao}" editado com sucesso!')
            return redirect('step:projectos')
        else:
            messages.error(
                request, f'{form.errors}', extra_tags='danger')
    else:
        form = FormProjecto(instance=obj)

    context = {'form': form, 'entidade': obj.entidade}
    return render(request, 'step/editarprojectos.html', context)




@login_required
def deleteProjecto(request, pk):
    obj = get_object_or_404(Projectos, pk=pk)
    obj.delete()
    # Criar mensagem de sucesso, pois a operação foi efectuada com sucesso.
    messages.success(
        request, f'Projecto "{obj.descricao}" eliminada com sucesso!')
    return redirect('step:projectos')
