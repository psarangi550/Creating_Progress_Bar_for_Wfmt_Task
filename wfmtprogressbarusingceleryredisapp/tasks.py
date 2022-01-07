from __future__ import absolute_import,unicode_literals
from celery import shared_task
from celery.utils.log import get_task_logger
from celery_progress.backend import ProgressRecorder
import time

logger=get_task_logger(__name__)

@shared_task(bind=True)
def duration(self):
    progress_recorder=ProgressRecorder(self)
    for i in range(10):
        time.sleep(1)
        progress_recorder.set_progress(i+1,10,f"completed {i+1} iteration of 10 ")
    return 5

@shared_task
def add(a,b):
    return a+b

    