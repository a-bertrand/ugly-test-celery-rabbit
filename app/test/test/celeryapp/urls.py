from django.contrib import admin
from django.urls import path
from .views import start_task_a, start_task_b

urls = [
    path('start-task-a/', start_task_a, name='start_task_a'),
    path('start-task-b/', start_task_b, name='start_task_b')
]
