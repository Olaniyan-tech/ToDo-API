from django.db import models
from django.conf import settings
from django.urls import reverse
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from .utils import slugify_instance_title
from django.utils import timezone

# Create your models here.

User = settings.AUTH_USER_MODEL

class TaskQueryset(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()
        lookups = Q(title__icontains = query)
        return self.filter(lookups)

class TaskManager(models.Manager):
    def get_queryset(self):
        return TaskQueryset(self.model, using=self._db)
    
    def search(self, query=None):
        return self.get_queryset().search(query=query)
        
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = TaskManager()

    def __str__(self):
        return self.title
    

#signals    
def todo_pre_save(sender, instance, *args, **kwargs):
    if instance.title:
        slugify_instance_title(instance, save=False)

pre_save.connect(todo_pre_save, sender=Task)







