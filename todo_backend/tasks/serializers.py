from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id","user","title","description","status","priority","due_date","reminder_time","created_at","updated_at")
        read_only_fields = ("id","user","created_at","updated_at")
