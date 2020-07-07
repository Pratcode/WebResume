from django.db import models


# Create your models here.


class Media(models.Model):
    media_name = models.CharField(max_length=100)
    media_pro = models.CharField(max_length=100)
    media_body = models.TextField(blank=True)
    media_img = models.ImageField(upload_to='image', default='default_img.jpg')
    media_file = models.FileField(upload_to='documents', default='default_file.pdf')
    facebook = models.URLField(max_length=300, blank=True)
    Twitter = models.URLField(max_length=300, blank=True)
    Google = models.URLField(max_length=300, blank=True)
    Linkedin = models.URLField(max_length=300, blank=True)
    Instagram = models.URLField(max_length=300, blank=True)
    Pinterest = models.URLField(max_length=300, blank=True)
    Stack_Overflow = models.URLField(max_length=300, blank=True)
    Youtube = models.URLField(max_length=300, blank=True)
    Slack = models.URLField(max_length=300, blank=True)
    Github = models.URLField(max_length=300, blank=True)
    Email = models.URLField(max_length=300, blank=True)
    Reddit = models.URLField(max_length=300, blank=True)

    def __str__(self):
        return self.media_name


class Contact(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField(max_length=300)
    contact_body = models.TextField()

    def __str__(self):
        return self.contact_name
