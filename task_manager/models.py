from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.exceptions import ValidationError



def due_date_validator(due_date):
    current_date = timezone.now()
    
    if  due_date < current_date:
        raise ValidationError(f"Your due date cannot be in the past or now, it has to be in the future")
    

User = get_user_model()

class status_choices(models.TextChoices):
    TODO = 'todo', 'To Do'
    IN_PROGRESS = 'inprogress', 'In Progress'

class priority_choices(models.TextChoices):
    HIGH = 'high', 'High'
    MEDIUM = 'medium', 'Medium'
    LOW = 'low', 'Low'


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(validators=[due_date_validator])
    status = models.CharField(max_length=20, choices=status_choices.choices, default=status_choices.TODO)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.CharField(max_length=20, choices=priority_choices.choices, default=priority_choices.MEDIUM)

    def __str__(self):
        return f'{self.title}'
