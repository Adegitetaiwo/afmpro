from django.db import models
from django.utils import timezone
from datetime import datetime
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

# Create your models here.
class displaySilder(models.Model):
    title = models.CharField(max_length=150)
    discriptionTop = models.CharField(blank = True, null=True, max_length=40)
    discriptionBottom = models.CharField(blank = True, null=True, max_length=100)
    displayImage = CloudinaryField()

    def __str__(self):
        return self.title


class sm_phone_display(models.Model):
    title = models.CharField(max_length=150)
    discriptionTop = models.CharField(blank=True, null=True, max_length=40)
    discriptionBottom = models.CharField(blank=True, null=True, max_length=100)
    displayImage = CloudinaryField()

    def __str__(self):
        return self.title
    

class setCountdownDate(models.Model):
    eventTitle = models.CharField(max_length=100)
    eventDate = models.DateTimeField(default=timezone.now, blank=True)
    eventDiscription = models.TextField()
    endTimeMessage = models.CharField(max_length=100)
    active = models.BooleanField()

    def __str__(self):
        return self.eventTitle

class userType(models.Model):
    createUserType = models.CharField(max_length=50, verbose_name= 'User Title')

    def __str__(self):
        return self.createUserType

class urgentMessage(models.Model):
    messageTitle =  models.CharField(max_length=50, verbose_name= 'Message Title')
    Active = models.BooleanField()
    UserTitle = models.ForeignKey(userType, verbose_name= "User Title", on_delete=models.CASCADE)
    userImage = CloudinaryField()
    date = models.DateTimeField(default=timezone.now, blank=True)
    likeCount = models.IntegerField(verbose_name= 'Likes Count')
    messageBody = RichTextField(verbose_name= 'Message Body')

    def __str__(self):
        return self.messageTitle

class sermonUpdate(models.Model):
    link = models.URLField(max_length=500, verbose_name= 'Link to Video Source (e.g Youtube.)')
    image = CloudinaryField(verbose_name = 'Image of a Scene During The Service')
    sermonTitle = models.CharField(max_length=100, verbose_name='Sermon Title')
    precherName = models.CharField(max_length=70, verbose_name='Officiating Minister')

    def __str__(self):
        return self.sermonTitle + ' by ' + self.precherName

class event(models.Model):
    theme = models.CharField(max_length=150)
    bible_ref = models.TextField()
    date = models.DateTimeField(default=timezone.now, blank=True)
    detail = models.TextField()
    active = models.BooleanField()
    
    def __str__(self):
        return self.theme
    
class subcribe(models.Model):
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.email
