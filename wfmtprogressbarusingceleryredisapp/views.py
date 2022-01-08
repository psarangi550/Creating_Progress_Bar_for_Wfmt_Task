from django.shortcuts import render
import time
from .tasks import duration
from django_celery_results.models import TaskResult
# Create your views here.

def index(request):
    task=duration.delay()
    # print(dir(result))
    # print(type(result))
    # task_id=result.task_id
    # worker=result.result
    # print(worker)
    # task_status=result.status
    # print(task_status)
    # print(task_id)
    # print(task)
    # print(type(task))
    # print(type(task.task_id))
    # task_id=TaskResult.objects.get(task_id=task.task_id)
    # context={"task_id":task.task_id}
    return render(request,"wfmtprogressbarusingceleryredisapp/index.html",{"task_id":task.task_id})