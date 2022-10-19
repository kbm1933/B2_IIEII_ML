from django.db import models
from users.models import User


# Create your models here.


class FileUpload(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    imgfile = models.ImageField(null=True, upload_to='images/', blank=True, editable=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class YoloResult(models.Model):
    imgs = models.ImageField(null=True, upload_to='images/', blank=True, editable=True)
    fruit_class = models.TextField(null=True)
    confidence = models.TextField(null=True)
