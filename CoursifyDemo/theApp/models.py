from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class DoubtModel(models.Model):

    username = models.CharField(max_length=264)
    subject = models.CharField(max_length=264)
    language = models.CharField(max_length=264)
    doubt = models.TextField()

    def __str__(self):

        return 'User: '+  self.username.upper() + ' Doubt: ' +  self.doubt

class ClarifyDoubtModel(models.Model):

    username = models.CharField(max_length=264)
    subject = models.CharField(max_length=264)
    doubt_pic = models.ImageField(upload_to='pics',blank=False)
    doubt = models.TextField()

    def __str__(self):

        return self.doubt
