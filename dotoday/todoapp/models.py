from django.db import models

# Create your models here.

class TaskToDo(models.Model):
    taskName = models.CharField(max_length=250)
    taskTime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.taskName
