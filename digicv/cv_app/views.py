from django.shortcuts import render
from django.http import HttpResponse
from cv_app import forms
#from . import forms

import os

# Create your views here.



def root_page(request):
    resume_contents = { 'resume_title': '''Python Cloud Developer. 11 years of industry experience in developing 
    applications using Python, Android | 
    AWS Certified solutions architect associate |
    Certified scrum master''',
                        'stack_url':'https://stackoverflow.com/users/5907578/dineshkumar',
                        'medium_url':'https://medium.com/@dineshkumarkb',
                        'linked_url':'https://www.linkedin.com/in/dineshkumar-k-b-b8853a24/',
                        'github_url':'https://github.com/dineshkumarkb',
                        'nav_link1':"Career",
                        'nav_link2':"Certifications",
                        'nav_link3':"Personal Projects",
                        "nav_link4":"Roles and Responsibilities"}

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
