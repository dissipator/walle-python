# -*- coding: utf-8 -*-
 
#from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	context = {}
	return render(request, 'site/login.html', context)

def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)