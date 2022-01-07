from __future__ import absolute_import,unicode_literals

from celery import Celery

import os 

os.environ['DJANGO_SETTINGS_MODULE'] ="wfmtprogressbarusingceleryredisproj.settings"

app=Celery("wfmtprogressbarusingceleryredisproj")

app.conf.enable_utc=False

app.conf.update(timezone="Asia/Kolkata")

app.config_from_object("django.conf:settings",namespace="CELERY")

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f" Request {self.request !r}")
    
    