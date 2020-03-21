from rest_framework import serializers
from .models import Module

class ModuleSerializer(serializers.ModelSerializer):
        class Meta:
                model=Module
                fields='__all__'


class ProfessorSerializer(serializers.Serializer):
        professor_id = serializers.CharField(max_length=20)
        name = serializers.CharField(max_length=20)
        #rating = serializers.IntegerField()