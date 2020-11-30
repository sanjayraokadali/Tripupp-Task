from django.db import models

# Create your models here.
class DoubtModel(models.Model):

    username = models.CharField(max_length=264)
    subject = models.CharField(max_length=264)
    language = models.CharField(max_length=264)
    doubt = models.TextField()

    def __str__(self):

        return 'User: '+  self.username.upper() + ' Doubt: ' +  self.doubt
