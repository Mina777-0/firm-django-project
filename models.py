from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.name} ({self.code})"
    

class Employee(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    department = models.ManyToManyField(Department, blank=True, related_name="posts")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
