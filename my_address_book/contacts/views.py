
# Create your views here.
from django.shortcuts import render, redirect
from .models import Address
from .forms import PersonForm, AddressForm
from django.db import models



def home(request):
    return redirect('search')

def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Address.objects.filter(models.Q(person__name__icontains=query) | models.Q(address__icontains=query))
    return render(request, 'search.html', {'results': results, 'query': query})  # Renders the 'search.html' template with the results and query variables passed to the template context.

def add_person(request):  
    if request.method == 'POST':   # Checks if the request method is 'POST'.
        person_form = PersonForm(request.POST)  # Initializes a PersonForm instance with the POST data from the request.
        address_form = AddressForm(request.POST)  #  Initializes an AddressForm instance with the POST data from the request.
        if person_form.is_valid() and address_form.is_valid(): #  Checks if both the person_form and address_form are valid.
            person = person_form.save()   #  Saves the person_form data to create a new Person object and returns the saved instance.
            address = address_form.save(commit=False)  # Saves the address_form data to create a new Address object but doesn't commit it to the database yet.
            address.person = person  # Associates the address with the person by assigning the person instance to the person field of address.
            address.save() # Saves the address instance, now with the associated person, to the database.
            return redirect('search')  # Redirects the request to the search view.
    else:      # If the request method is not 'POST':
        person_form = PersonForm()  # Initializes an empty PersonForm instance.
        address_form = AddressForm()  #  Initializes an empty AddressForm instance.
    return render(request, 'add_person.html', {'person_form': person_form, 'address_form': address_form})
       # Renders the 'add_person.html' template with the person_form and address_form variables passed to the template context.