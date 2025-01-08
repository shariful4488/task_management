from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Hello, World!')
def contact(request):
    return HttpResponse('Contact page')

def show_task(request):
    return HttpResponse('This is a task')