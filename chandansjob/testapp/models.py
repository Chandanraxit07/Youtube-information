from django.db import models

# Create your models here.
class Hydjobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    eligibility = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()


class Punejobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    eligibility = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()

class Bangjobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    eligibility = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()