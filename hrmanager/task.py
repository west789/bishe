import time
from celery import task
import django
django.setup()

@task
def sayHi():
    print('第一次出现hello')
    time.sleep(5)
    print("5秒后出现world")