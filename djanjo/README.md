# django_basic
It will tell how to use a django project and implement it

Step 1 : open anaconda prompt
Step 2: create a new folder
(base) C:\Users\dhruv\Desktop>mkdir My_Django_Stuff

Step 3: Enter into it
(base) C:\Users\dhruv\Desktop>cd My_Django_Stuff

Step 4: create a vin environment
(base) C:\Users\dhruv\Desktop\My_Django_Stuff>activate myDjangoEnv

You can list all discoverable environments with `conda info --envs`.

Step 5: start a new project
(myDjangoEnv) C:\Users\dhruv\Desktop\My_Django_Stuff>django-admin startproject first_project

Step 6:(myDjangoEnv) C:\Users\dhruv\Desktop\My_Django_Stuff>cd first_project

Step 7 : runserver
(myDjangoEnv) C:\Users\dhruv\Desktop\My_Django_Stuff\first_project>python manage.py runserver

Step 8: create a project where u can work
(myDjangoEnv) C:\Users\dhruv\Desktop\My_Django_Stuff\first_project>python manage.py startapp hello_world

Step 9: go to settings in first project and add hello_world in  Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hello_world'
]

Step 10 : Go to views.py in hello_world
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return HttpResponse("Hello World!")
  
  
Step 11: Go to urls.py in first_project
from django.contrib import admin
from django.urls import path,re_path
from hello_world import views

urlpatterns = [
	re_path('$',views.index,name = 'index'),
    path('admin/', admin.site.urls),
]

Step 12:Implement
python manage.py runserver
