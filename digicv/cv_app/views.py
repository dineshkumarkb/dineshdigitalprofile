from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def root_page(request):
    return HttpResponse(" Welcome to the root page ")
