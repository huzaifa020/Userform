from django.http import *
from django.shortcuts import *
from django.core.paginator import *
from django import *
from django.shortcuts import render
from form.models import form
def homepage(request):
    if request.method == 'POST':
        # Retrieve data from the POST request
        # The keys here ('field1', 'field2', etc.) must match the 'name' attributes
        # of the input fields in your HTML form.
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # ... retrieve other fields as needed

        # Perform basic validation (e.g., check if fields are not empty)
        if not name or not email or not password:
            # You might want to display an error message here
            return render(request, 'index.html', {'error': 'All fields are required'})

        # Save the data to the database
        try:
            # 1. Create a new instance of your model
            new_entry = form(
                name=name,
                email=email,
                password=password,
                # ... map other form data to model fields
            )
            # 2. Save the instance to the database
            new_entry.save()

            # Redirect the user to a success page or another relevant page
            return redirect('success_url_name') # Replace with your success URL name
        
        except Exception as e:
            # Handle any database errors
            print(f"Database Error: {e}")
            return render(request, 'index.html', {'error': 'A database error occurred.'})
    # if request.method == "POST":
    #     if request.POST.get('name', 'email', 'password') == "":
    #         return render(request, 'contact.html', {'error': True})
    # # To save form data in database
    # if request.method == "POST":
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     meta = userform(name=name, email=email, password=password)
    #     meta.save()
    return render(request,"index.html")