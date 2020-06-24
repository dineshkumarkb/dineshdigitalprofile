from django.shortcuts import render
from django.http import HttpResponse
from cv_app import forms
#from . import forms

import os

# Create your views here.



def root_page(request):
    resume_contents = { 'resume_title': '''Python Cloud Developer.AWS Certified solutions architect associate.
    Certified scrum master'''

    }
    print(request)
    return render(request,'cv_app/landing.html',context=resume_contents)


def form_page(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print(" Form validation successful ")
            print(f" Name is {form.cleaned_data.get('name')}")
        return HttpResponse(" Form data received ")
    return render(request,'cv_app/myform.html',context={'form':form})
