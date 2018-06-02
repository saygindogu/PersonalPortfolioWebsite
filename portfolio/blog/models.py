from django.db import models

# Create your models here.

class BlogPost( models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    body = models.TextField()
    publication_date = models.DateTimeField()
