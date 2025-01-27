from rest_framework import serializers

from .models import Todoitem

class TodoitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todoitem
        fields = ['id','title' ,'description', 'due_time', 'completed', 'created_at', 'updated_at']
