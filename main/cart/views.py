from django.conf import settings
from django.shortcuts import render, redirect
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
        
        handle_inquiry(name, phone, email, people, travel_date)
        
        messages.success(request, 'Thank you for your inquiry! A confirmation email has been sent to you.')
        
        return redirect('home')
    
    return render(request, 'index.html')

def modal(request):
    if not settings.SHOW_MODAL:
        return redirect('home')
    
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        people = request.POST.get('people')
        travel_date = request.POST.get('travel_date')

        handle_inquiry(name, phone, email, people, travel_date)

        messages.success(request, 'Thank you for your inquiry! A confirmation email has been sent to you.')

        return redirect('home')
      
    return render(request, 'modal.html')

def packages(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        people = request.POST.get('people')
        travel_date = request.POST.get('travel_date')
        
        handle_inquiry(name, phone, email, people, travel_date)
        
        messages.success(request, 'Thank you for your inquiry! A confirmation email has been sent to you.')
        
        return redirect('packages')
    
    return render(request, 'packages.html')
