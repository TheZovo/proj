from django.contrib import admin
from todo_list.models import ToDoItem
# Register your models here.
@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    list_display = "id", "title", "Done"