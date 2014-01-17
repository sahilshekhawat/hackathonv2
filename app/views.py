# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from google.appengine.api import users
import os
import sys

def home(request):
    return render(request, 'index.html', {})

def user_home(request):
    if users:   
    	filedir = sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
    	user_function = users.get_current_user()  
    	email = user_function.email()
    	username = user_function.nickname()
    	href = users.create_logout_url('/')
    	link = "logout"
     	return render(request, 'home.html', { 'href': href, 'link': link, 'email': email, 'username': username, 'filedir': filedir})


