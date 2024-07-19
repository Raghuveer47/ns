from django.urls import path
from . import views

urlpatterns = [
    path('', views.modal, name="modal"),  # Default path to open the modal first
    path('home/', views.home, name="home"),  # Path to home page after form submission
]
