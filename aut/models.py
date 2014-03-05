import json
from django.db import models

# Create your models here.
import twython
from twython_django_oauth.models import TwitterProfile
from tapp.settings import TWITTER_SECRET, TWITTER_KEY


class TwitterProfileCredentials(models.Model):
    twitterprofile = models.OneToOneField(TwitterProfile)
    data = models.TextField()

    data_obj = None

    def __getitem__(self, item):
        if self.data_obj==None:
            self.data_obj = json.loads(self.data)
        return self.data_obj[item]

    def twython(self):
        return twython.Twython(TWITTER_KEY,TWITTER_SECRET,self.twitterprofile.oauth_token,self.twitterprofile.oauth_secret)


