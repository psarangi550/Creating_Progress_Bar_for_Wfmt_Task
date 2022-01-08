from __future__ import absolute_import,unicode_literals
from celery import shared_task
from celery.utils.log import get_task_logger
from celery_progress.backend import ProgressRecorder
import time

logger=get_task_logger(__name__)

@shared_task(bind=True)
def duration(self):
    progress_recorder=ProgressRecorder(self)
    for i in range(20):
        time.sleep(2)
        progress_recorder.set_progress(i+1,20,f"completed {i+2} iteration of 20 ")

@shared_task
def add(a,b):
    return a+b

    