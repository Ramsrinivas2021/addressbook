from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Address(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    address = models.TextField()

    def __str__(self):
        return f"{self.person.name}'s Address"
