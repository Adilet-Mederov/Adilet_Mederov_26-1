from django.shortcuts import HttpResponse, redirect
from datetime import datetime

# Create your views here.

def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello, its my project!')



def now_date_view(request):
    if request.method == 'GET':
        return HttpResponse(f'{datetime.now()}')


def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse("Goodbye User!")