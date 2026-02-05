from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255, required=False)
    due_at = serializers.DateTimeField(required=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'due_at', 'created_at', 'updated_at', 'created_by')
