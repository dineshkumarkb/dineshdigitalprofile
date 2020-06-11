from django.shortcuts import render
from django.http import HttpResponse

import os

# Create your views here.



def root_page(request):
    resume_contents = { 'resume_title': '''Python Cloud Developer.AWS Certified solutions architect associate.
    Certified scrum master'''

    }
    print(request)
    return render(request,'cv_app/landing.html',context=resume_contents)
