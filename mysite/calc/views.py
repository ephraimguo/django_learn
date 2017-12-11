from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def add(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    c = int(a) + int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def index(request):
    str1 = ['welcome', 'this is line 1', 'this is line 2', 'this is line 3']
    info_dict = {'site':u'citygate_welcom', 'content':u'all the faith based videos'}
    return render(request, 'calc/home.html', {'str2':str1, 'info_dict': info_dict})







