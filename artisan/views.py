from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from XOXOXO.models import XOXOXO

class XOXOXOForm(ModelForm):
    class Meta:
        model = XOXOXO
        fields = []

def index(request, template_name='XOXOXO/index.html'):
    object = XOXOXO.objects.all()
    data = {}
    data['object_list'] = object
    return render(request, template_name, data)

def show(request, template_name='XOXOXO/show.html'):
    object = get_object_or_404(XOXOXO, pk=pk)
    data = {}
    data['object_list'] = object
    return render(request, template_name, data)

def create(request, template_name='XOXOXO/create_form.html'):
    form = XOXOXOForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index_XOXOXO')
    return render(request, template_name, {'form':form})

def update(request, pk, template_name='XOXOXO/create_form.html'):
    object = get_object_or_404(XOXOXO, pk=pk)
    form = XOXOXOForm(request.POST or None, instance=object)
    if form.is_valid():
        form.save()
        return redirect('index_XOXOXO')
    return render(request, template_name, {'form':form})

def delete(request, pk, template_name='XOXOXO/confirm_delete.html'):
    object = get_object_or_404(XOXOXO, pk=pk)
    if request.method=='POST':
        object.delete()
        return redirect('index_XOXOXO')
    return render(request, template_name, {'object':object})