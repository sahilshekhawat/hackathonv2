import datetime
from google.appengine.ext import ndb, db
from google.appengine.api import users

class UserData(ndb.Model):
    username = ndb.StringProperty()
    email = ndb.StringProperty()
    

class Time(ndb.Model):
    time = ndb.DateTimeProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

class Profile(db.Model):
    contributed_to = db.StringProperty()
    paid = db.IntegerProperty()
    started = db.StringProperty()
    picture = db.BlobProperty()


class Post(db.Model):
    description = db.TextProperty()
    title = db.StringProperty()
    payment = db.IntergerProperty()
    





    
