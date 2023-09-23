from django.shortcuts import render
from .models import projects
from django.conf import settings
from django.http import FileResponse
import os

def home(request):
  project=projects.objects.all()
  data={
    'projects':project
  }
  return render(request,"index.html",data)

def download_file(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'cv.pdf')
    return FileResponse(open(file_path, 'rb'), as_attachment=True)