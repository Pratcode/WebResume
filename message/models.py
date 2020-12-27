from django.db import models


# Create your models here.


class Message(models.Model):
    Message_name = models.CharField(max_length=100)
    Message_email = models.EmailField(max_length=300)
    Message_body = models.TextField()

    def __str__(self):
        return self.Message_name
