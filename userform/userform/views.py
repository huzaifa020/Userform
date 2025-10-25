from django.http import *
from django.shortcuts import *
from django.core.paginator import *
from django import *
from django.shortcuts import render
def home(request):
    return render (request, 'userform/index.html')