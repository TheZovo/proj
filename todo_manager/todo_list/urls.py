
from django.views.generic import TemplateView
from django.urls import path

from . import views

app_name = 'todo_list'

urlpatterns = [
    # path("", views.index_view(), name = 'index'),
    # path("", views.ToDoListIndexView.as_view(), name = 'index'),
    path("", views.ToDoListView.as_view(), name="index")
]
