from __future__ import absolute_import,unicode_literals
from celery import shared_task
from celery.utils.log import get_task_logger
from celery_progress.backend import ProgressRecorder
import time

logger=get_task_logger(__name__)

@shared_task(bind=True)
def duration(self):
    progress_recorder=ProgressRecorder(self)
    logger.info(f"This task will go for sleep with duration metioned")
    result=0
    for i in range(10):
        time.sleep(1)
        result=result+i
        progress_recorder.set_progress(i+1,10,description=f"completed {i+1} iteration of 5")
    return "completed task"
    