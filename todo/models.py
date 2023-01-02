from django.db import models

# Create your models here.



class Todo(models.Model):
    todo = models.CharField(max_length=200)
    description = models.TextField()
    type = models.ForeignKey('Type', on_delete=models.CASCADE)

    def __str__(self):
        return self.todo



class Type(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type

