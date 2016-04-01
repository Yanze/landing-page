from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.TextField(max_length=100)
    interest =  models.TextField(max_length=200)
    favo_language = models.TextField(max_length=200)
    class Meta:
        db_table = 'person'
