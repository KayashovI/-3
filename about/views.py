from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'about')