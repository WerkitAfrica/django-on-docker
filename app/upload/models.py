from django import forms
from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Invoice(models.Model):
    invoice_id = models.CharField(blank=True, max_length=8)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    csv = models.FileField()

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Email(models.Model):
    freelancer = models.ForeignKey(Person, on_delete=models.CASCADE)
    email = models.EmailField(max_length=70)

class Payment(models.Model):
    amount = models.DecimalField(max_digits=20, decimal_places=3)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    paid = models.BooleanField()
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    

