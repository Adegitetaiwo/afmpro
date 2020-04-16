from django.db import models
from account.views import User
from django import forms
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

# Create your models here.


class blog(models.Model):
    blogTitle = models.CharField(max_length=50, verbose_name= 'Blog Tile')
    blogSubtile = models.TextField(blank=True, null=True, verbose_name= 'Subtitle[if any]')
    featuredImage = CloudinaryField()
    likeCount = models.IntegerField(blank=True, null=True)
    blogBody = RichTextField(blank=True, null=True, verbose_name= 'Body')
    username = models.CharField(max_length=100)
    userPicture = CloudinaryField()
    aboutUser = RichTextField()
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.blogTitle

    @property
    def get_comments(self):
        return self.comments.all()


class Comment(models.Model):
    name = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(blog, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
