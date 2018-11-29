from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def index(request):
    """display index describing the application"""
    template_name = 'index.html'
    return render(request, template_name)
