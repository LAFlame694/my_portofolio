from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, 'base.html')

def base_view(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = f"Portofolio Contact from {name}"
        full_message = f"Name: {name}\nEmail: {email}\nMessage: {message}"

        send_mail(
            subject,
            full_message,
            settings.DEFAULT_FROM_EMAIL, # sender
            [settings.CONTACT_EMAIL], # recipient
            fail_silently=False,
        )
        success = True
    
    return render(request, 'base.html', {'success': success})