from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Inquiry
from .helpers import handle_inquiry

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        people = request.POST.get('people')
        travel_date = request.POST.get('travel_date')
        
        # Handle the inquiry using the helper function
        handle_inquiry(name, phone, email, people, travel_date)
        
        # Add success message
        messages.success(request, 'Thank you for your inquiry! A confirmation email has been sent to you.')
        
        return redirect('home')
    
    return render(request, 'index.html')

def modal(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        people = request.POST.get('people')
        travel_date = request.POST.get('travel_date')

        # Handle the inquiry using the helper function
        handle_inquiry(name, phone, email, people, travel_date)

        # Add success message
        messages.success(request, 'Thank you for your inquiry! A confirmation email has been sent to you.')

        # Redirect to the home page
        return redirect('home')
      
    return render(request, 'modal.html')
