from django.db import models

# Create your models here.


class People(models.Model):

    First_Name = models.CharField(max_length=60)
    Last_Name = models.CharField(max_length=60)
    Address = models.CharField(max_length=120)
    DateO_of_Birth = models.DateField()
    image_url = models.CharField(max_length=2034)


