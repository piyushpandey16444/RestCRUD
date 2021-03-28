from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=250)
    roll_no = models.IntegerField()
    city = models.CharField(max_length=250)

    def __str__(self):
        return self.name
