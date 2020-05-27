from django.http import HttpRespose
from django.shortcuts import redirect

def index(request):
    return HttpResponse('infex')

def login(request):
    return redirect('/index')
