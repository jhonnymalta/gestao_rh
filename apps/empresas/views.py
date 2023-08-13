from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView
from .models import Empresa


@login_required
def nova(request):
    return render(request,'empresas/nova.html')


class EmpresaCreateViewModel(CreateView):
    model = Empresa
    fields = ['nome']

    def form_valid(self, form):
        form.save()
        return  HttpResponse('OK')

class EmpresaEditViewModel(UpdateView):
    model = Empresa
    fields=['nome']

    def form_valid(self, form):
        form.save()
        return HttpResponse('OK')
