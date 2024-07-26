import time
from celery import shared_task
import datetime
@shared_task
def send_emails():
   for x in range(10):
        print(x)
        time.sleep(1)
