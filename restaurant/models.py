from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    date_opened = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    opening_hour = models.TimeField(blank=True, null=True)
    closing_hour = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    date_birth = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE, blank=True, null=True)

class Table(models.Model):
    number = models.IntegerField(blank=True, null=True)
    chairs = models.IntegerField(blank=True, null=True)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.number)


class Reservation(models.Model):
    table = models.ForeignKey('Table', on_delete=models.CASCADE, blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.table.number) + " - " + self.name

