from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from .models import Inquiry

def handle_inquiry(name, phone, email, people, travel_date):
    # Save inquiry to the database
    inquiry = Inquiry.objects.create(
        name=name,
        phone=phone,
        email=email,
        people=people,
        travel_date=travel_date
    )

    # Send welcome email to the user
    subject_user = "Welcome to NS Tours"
    message_user = render_to_string('email/welcome_email.html', {'name': name})
    email_user = EmailMessage(subject_user, message_user, settings.EMAIL_HOST_USER, [email])
    email_user.content_subtype = "html"
    email_user.send()

    # Send notification email to the admin
    subject_admin = "New Trip Inquiry"
    message_admin = render_to_string('email/admin_notification.html', {
        'name': name,
        'phone': phone,
        'email': email,
        'people': people,
        'travel_date': travel_date
    })
    admin_email = settings.EMAIL_HOST_USER
    email_admin = EmailMessage(subject_admin, message_admin, settings.EMAIL_HOST_USER, [admin_email])
    email_admin.content_subtype = "html"
    email_admin.send()
