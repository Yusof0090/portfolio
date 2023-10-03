from django.urls import path
from . import views
from .views import download_file

urlpatterns = [
	path('', views.home, name="home"),
    path('download/', download_file, name='download'),
    
	]