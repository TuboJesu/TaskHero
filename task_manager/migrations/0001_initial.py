# Generated by Django 5.2 on 2025-04-18 10:35

import django.db.models.deletion
import task_manager.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('due_date', models.DateTimeField(validators=[task_manager.models.due_date_validator])),
                ('status', models.CharField(choices=[('todo', 'To Do'), ('inprogress', 'In Progress')], default='todo', max_length=20)),
                ('completed', models.BooleanField(default=False)),
                ('priority', models.CharField(choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], default='medium', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
