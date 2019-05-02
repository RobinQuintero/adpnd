from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from evaluador.evaluador import Evaluador
import json
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
@csrf_exempt
def evaluador(request, palabra):
    if request.method == 'GET':
        eval = Evaluador().evaluar(palabra)
        return JSONResponse(eval.__dict__, status=200)
    if request.method == 'POST':
        return HttpResponse(status=403)
