from django.db import models

# Create your models here.

class TaskToDo(models.Model):
    taskName = models.CharField(max_length=250)
    def __str__(self):
        return self.taskName
