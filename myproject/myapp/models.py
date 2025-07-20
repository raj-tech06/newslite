# models.py
from django.db import models

class News(models.Model):
    CATEGORY_CHOICES = [
        ('adhikar', 'आपका अधिकार'),
        ('bharat', 'भारत'),
        ('janata', 'जनता की आवाज़'),
        ('local', 'लोकल खबरें'),
        ('international', 'अंतर्राष्ट्रीय'),
        ('opinion', 'ओपिनियन'),
        ('politics', 'राजनीती'),
        ('education', 'शिक्षा'),
        ('society', 'समाज'),
        ('cyber', 'साइबर सुरक्षा'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    category_slug = models.SlugField()  # Ya CharField ho sakta hai

    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    video = models.FileField(upload_to='news_videos/', blank=True, null=True)


    def __str__(self):
        return self.title
