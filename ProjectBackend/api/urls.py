from django.urls import path
from . import views

urlpatterns = [
    path('tasks', views.GetTasks), 
    path('tasks/', views.GetTask),
]