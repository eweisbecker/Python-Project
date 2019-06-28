from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from datetime import datetime 
import re

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class User(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=20)

class Project(BaseModel):
    title = models.CharField(max_length=50)
    description = models.TextField()
    deadline = models.DateField(default=timezone.now)
    done = models.BooleanField(default=False)
    members = models.ManyToManyField(User, related_name="joined_group")
    creator = models.ForeignKey(User, related_name="created_project")

class Task(BaseModel):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    status = models.TextField(default="to_do")
    priority = models.IntegerField()
    tasks = models.ForeignKey(Project, related_name="added_task")
    creator = models.ForeignKey(User, related_name="created_task")