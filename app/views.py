# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from google.appengine.api import users
from models import date
from models import account
