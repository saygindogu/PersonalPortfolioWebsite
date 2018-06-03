from django.db import models

# Create your models here.

class BlogPost( models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    body = models.TextField()
    publication_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def summary(self):
        dots = ''
        if len( self.body ) > 100:
            dots = '...'
        return self.body[:100] + dots

    def pretty_publication_date(self):
        return self.publication_date.strftime( '%b %e %Y')
