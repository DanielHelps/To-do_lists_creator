from django.db import models


# Create your models here.
class ToDoL(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoL, on_delete=models.CASCADE, related_name='items')
    to_do_text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.to_do_text
