from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField

# Create your models here.
class liveForcast(models.Model):
    title = models.CharField(max_length=100)
    introduction = models.TextField(default=True, blank=True)
    date = models.DateTimeField(default=timezone.now, blank=True)
    watching = models.IntegerField()
    image = CloudinaryField()
    source = models.URLField(max_length=500)
    active = models.BooleanField()

    def __str__(self):
        return self.title
