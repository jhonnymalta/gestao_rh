import json

from django.http import HttpResponse
from django.shortcuts import render


from  django.views.generic import View
# Create your views here.

class registrar_ponto(View):

    def post(self,pk):
        response = json.dumps({'mensagem':'requisicao executada'})
        return  HttpResponse(response,content_type='application/json')

