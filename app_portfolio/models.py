from django.db import models

class PortfolioItem(models.Model):
    title = models.CharField(max_length=100)
    filter = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='galerie/')

    def __str__(self):
        return self.title
