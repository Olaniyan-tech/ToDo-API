from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Task

User = get_user_model()

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ['title', 'slug']
        read_only_fields = ['slug']

    def validate_title(self, value):
        user = self.context['request'].user
        if Task.objects.filter(user=user, title__iexact=value).exists():
            raise serializers.ValidationError(f"Task '{value}' is already in use. Please input a new title")
        return value
    
    
class TaskDetailsSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'slug', 'completed', 'date_created', 'updated']
        read_only_fields = ['id', 'user', 'slug', 'date_created', 'updated']


