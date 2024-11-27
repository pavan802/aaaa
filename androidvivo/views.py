from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vivo(request):
    return HttpResponse('android is  operating system of vivo')
