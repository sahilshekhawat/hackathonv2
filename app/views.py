# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from google.appengine.api import users
from models import date
from models import account
import os
import sys


def home(request):
    if user:   
    filedir = sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
    user = account()
    user_function = users.get_current_user()  
    user.email = user_function.email()
    user.username = user_function.nickname()
    href = users.create_logout_url('/')
    link = "logout"
        return render(request, 'home.html', { 'href': href, 'link': link, 'email': user.email, 'username': user.username, 'filedir': filedir})


