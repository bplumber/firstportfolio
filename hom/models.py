from django.db import models

class projects(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='pics')
    work= models.TextField()
    software = models.CharField(max_length=100)
    best = models.BooleanField(default=False)
    show = models.BooleanField(default=True)

class About(models.Model):
    describe = models.TextField()
    image = models.ImageField(upload_to='pics')

