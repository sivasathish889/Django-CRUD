from django.db import models

# Create your models here.
class Student(models.Model):
    Sname=models.CharField(max_length=20)
    SrollNo=models.IntegerField()
    Sclass=models.IntegerField()
    Snative=models.CharField(max_length=50)
    def __str__(self):
        return self.Sname

