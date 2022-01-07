from django.shortcuts import render
import time
from .tasks import duration
# Create your views here.

def index(request):
    task=duration.delay()
    print(task.get())
    print(task.status)
    print(task)
    print(type(task))
    # context={"task_id":task.task_id}
    return render(request,"wfmtprogressbarusingceleryredisapp/index.html",{"task_id":task.task_id})