from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


def index(request):
    return render(request, 'Home/index.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"""
New Contact Message

Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}
"""

        # Send mail to admin
        send_mail(
            subject,
            full_message,
            settings.DEFAULT_FROM_EMAIL,
            ['bilalshajamali@gmail.com'],
            fail_silently=False,
        )

        # Auto-reply to sender
        send_mail(
            "Thank you for contacting me",
            "I received your message. I will get back to you soon.",
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=True,
        )

        messages.success(request, "Your message has been sent successfully.")
        return redirect('index')

    return redirect('index')
