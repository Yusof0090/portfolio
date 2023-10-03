from django.shortcuts import render
from .models import projects
from django.conf import settings
from django.http import FileResponse
import time
import webbrowser
import os
import smtplib
from email.message import EmailMessage

def home(request):
    if request.method == 'POST':
        # Get the form data
        subject = request.POST.get('subject')
        message1 = request.POST.get('message')
        email = request.POST.get('recipient')
        message=f' Name:{subject},\n Email: {email},\n Message:{message1}'
        recipient = 'yusof.shokohyan4@gmail.com'

        # Create the email message
        email = EmailMessage()
        email['Subject'] = subject
        email['From'] = settings.EMAIL_HOST_USER
        email['To'] = recipient
        email.set_content(message)

        # Send the email using SMTP
        with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as smtp:
            smtp.starttls()
            smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            smtp.send_message(email)

        return render(request, 'success.html')

    project=projects.objects.all()
    data={
      'projects':project
    }
    return render(request,"index.html",data)

def contact(request):
    return render(request,'success.html')

def download_file(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'cv.pdf')
    return FileResponse(open(file_path, 'rb'), as_attachment=True)