from rest_framework import serializers
from .models import Module

class ModuleSerializer(serializers.ModelSerializer):
        class Meta:
                model=Module
                #fields='__all__'
                fields=('module_id','year')