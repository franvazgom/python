from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'created', 'updated')
        read_only_fields = ('created', 'updated',)

class SumaSerializer(serializers.Serializer):
    num1 = serializers.IntegerField()
    num2 = serializers.IntegerField()

class ProjectParameterSerializer(serializers.Serializer):
    parameters = serializers.JSONField()