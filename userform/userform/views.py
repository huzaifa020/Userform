from django.http import *
from django.shortcuts import *
from django.core.paginator import *
from django import *
from django.shortcuts import render
def index(request):
    return render(request,'index.html')