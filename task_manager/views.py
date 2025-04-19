from django.shortcuts import render
from django.utils import timezone
from utils.login_decorator import custom_login_required


from .models import Task

def landing_page(request):
    return render(request, 'task_manager/home.html')

@custom_login_required
def all_tasks(request):
    tasks = Task.objects.filter(user=request.user)
    now = timezone.now()

    overdue = tasks.filter(due_date__lt=now, completed=False)
    todo = tasks.filter(status='todo', due_date__gte=now)
    inprogress = tasks.filter(status='inprogress', due_date__gte=now)
    completed = tasks.filter(completed=True)

    context = {
        'overdue': overdue,
        'todo': todo,
        'in_progress': inprogress,
        'completed': completed,
    }
    return render(request, 'task_manager/all_tasks.html', context)
