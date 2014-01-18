# Create your views here.
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from google.appengine.api import users
import os
import sys
import models


def user_home(request):
    user_function = users.get_current_user() 
    filedir = sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))      
 
    if user_function:
        username = user_function.nickname()  
        email = user_function.email()
        href = users.create_logout_url('/')
        if (not models.UserData.query(
                models.UserData.username == user_function.nickname(),
                models.UserData.email == user_function.email()).get()):
            query = models.UserData(username=user_function.nickname(), email=user_function.email())
            query.put()
    else:
        username = user_function.nickname()
        email = user_function.email()
        href = users.create_login_url('/')
    return render(request, 'home.html', { 'href': href, 'email': email, 'username': username, 'filedir': filedir})



