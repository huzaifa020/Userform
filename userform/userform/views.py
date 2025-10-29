from django.http import *
from django.shortcuts import *
from django import *
from django.shortcuts import render
from form.models import form
from django.db import IntegrityError
def homepage(request):
    if request.method == 'POST':
        # Retrieve data from the POST request
        name = request.POST.get('name')
        email = request.POST.get('email1')
        password = request.POST.get('password')
        # Save the data to the database
        try:
            # 1. Create a new instance of your model
            new_entry = form(
                name=name,
                email=email,
                password=password,
            )
            # 2. Save the instance to the database
            new_entry.save()
        except Exception as e:
            # Handle any database errors
            print(f"Database Error: {e}")
            return redirect(request, 'index.html')
        
    return render(request,"index.html")