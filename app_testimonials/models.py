from django.db import models
from django.urls import reverse

class Testimonial(models.Model):
    content = models.TextField()  
    author = models.CharField(max_length=100)  
    designation = models.CharField(max_length=100)  
    image = models.ImageField(upload_to='galerie/', null=True, blank=True) 

    def __str__(self):
        return self.author + ' - ' + self.designation
    
    def get_add_testimonial_url(self):
        return reverse('add_testimonial')