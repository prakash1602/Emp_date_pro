from django.db import models


class EmployeeData(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    exp = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    salary = models.IntegerField()
    email = models.EmailField(max_length=100)
