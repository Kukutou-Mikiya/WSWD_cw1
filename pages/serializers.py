from rest_framework import serializers
from .models import Module
'''
class ModuleSerializer(serializers.ModelSerializer):
        class Meta:
                model=Module
                fields='__all__'
'''

class ProfessorSerializer(serializers.Serializer):
        professor_id = serializers.CharField(max_length=20)
        name = serializers.CharField(max_length=20)
        #rating = serializers.IntegerField()

class ModuleSerializer(serializers.Serializer):
        module_id = serializers.CharField(max_length=6)
        name = serializers.CharField(max_length=30)
    

class ModuleInstanceSerializer(serializers.Serializer):
        module = ModuleSerializer()
        year = serializers.IntegerField()
        semester = serializers.IntegerField()
        professor = ProfessorSerializer(many=True)      

