from django.shortcuts import render
from django.http import HttpResponse
import time
from test.celery import app as celery_app


def start_task_a(request):    
    task_b.apply_async()
    task_b.apply_async()
    task_b.apply_async()
    task_c.apply_async()
    task_a.apply_async()
    task_a.apply_async()
    task_c.apply_async()
    task_a.apply_async()
    task_c.apply_async()
    task_a.apply_async()
    task_c.apply_async()
    return HttpResponse("ok")


@celery_app.task(queue='tasks', priority=5)
def task_a():
    print("START TASK A")
    time.sleep(5)
    return "FINISH"

@celery_app.task(queue='tasks', priority=1)
def task_b():
    print("START TASK B")
    time.sleep(10)
    return "FINISH"

@celery_app.task(queue='tasks', priority=3)
def task_c():
    print("START TASK C")
    time.sleep(6)
    return "FINISH"



def start_task_b(request):
    return HttpResponse("ok")