from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Tasks

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model= Tasks
        fields=['id', 'type', 'title','description',"due_date",'remainder','created_at','finised']
        #read_only_fields=('created_at')

class TasksSerializer2(serializers.ModelSerializer):
    class Meta:
        model= Tasks
        fields=['id', 'type', 'title','finised']