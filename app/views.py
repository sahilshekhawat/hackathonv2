# Create your views here.
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from google.appengine.api import users
import os
import sys


def user_home(request):
    user_function = users.get_current_user() 
    if user_function:
        filedir = sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
        username = user_function.nickname()       
        email = user_function.email()
        href = users.create_logout_url('/')
        link = "logout"
        if (not models.UserData.query(
                models.UserData.username == user_function.nickname(),
                models.UserData.email == user_function.email()).get()):
            query = models.Query(username=user_function.nickname(), email=user_function.email())
            query.put()
            
            
    return render(request, 'home.html', { 'href': href, 'link': link, 'email': email, 'username': username, 'filedir': filedir})

        




