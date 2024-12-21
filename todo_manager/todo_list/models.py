from django.db import models

# Create your models here.
class ToDoItem(models.Model):
    class Meta:
        ordering = "id",
        verbose_name_plural = 'ToDo Items'
    title = models.CharField(max_length=250)
    Done = models.BooleanField(default=False)

    def __str__(self):
        return self.title