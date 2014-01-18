import datetime
from google.appengine.ext import ndb
from google.appengine.api import users

class UserData(ndb.Model):
    username = ndb.StringProperty()
    email = ndb.StringProperty()
    

class Time(ndb.Model):
    time = ndb.DateTimeProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

class Post(ndb.Model):




    
