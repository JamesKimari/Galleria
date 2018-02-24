from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']


