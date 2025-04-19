from django.urls import path
from . import views


app_name = 'task_manager'

urlpatterns = [
    path('', views.landing_page, name='home'),
    path('all/tasks', views.all_tasks, name='all_tasks'),
]