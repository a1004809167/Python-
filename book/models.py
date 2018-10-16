from django.db import models

# Create your models here.


class Book(models.Model):
    bookName = models.CharField(max_length=150)
    bookRate = models.CharField(max_length=50)
    bookDate = models.DateTimeField(null=True, blank=True)

class User(models.Model):
    username = models.CharField(max_length=20)  # CharField相当于字符串
    password = models.CharField(max_length=999)