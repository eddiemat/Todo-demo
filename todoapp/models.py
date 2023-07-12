from django.db import models

# Create your models here.

class Task(models.Model):
    taskName= models.CharField(max_length=100)
    description= models.CharField(max_length=500, blank=True)
    is_completed = models.BooleanField(default=False)
    is_deleted= models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    file=models.FileField

    def __str__(self):
        return self.taskName

    class Meta:
        db_table="task"
        ordering =['-created_at']


