from django.db import models


# Create your models here.


class Data(models.Model):
    data_title = models.CharField(max_length=100)
    data_body1 = models.TextField()
    data_body2 = models.TextField()
    data_body3 = models.TextField()
    data_body4 = models.TextField()

    def __str__(self):
        return self.data_title



