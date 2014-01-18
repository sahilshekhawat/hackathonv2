from google.appengine.ext import ndb

class UserData(ndb.Model):
    username = ndb.StringProperty()
    email = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
    contributed_to = ndb.StringProperty()
    paid = ndb.IntegerProperty()
    started = ndb.StringProperty()
    picture = ndb.BlobProperty()
    description = ndb.TextProperty()
    title = ndb.StringProperty()
    payment = ndb.IntegerProperty()
