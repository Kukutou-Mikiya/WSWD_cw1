from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Module
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ModuleSerializer
# Create your views here.
def GetModule(request):
        return HttpResponse("hello hello")

class HomePageView(ListView):
        model = Module
        template_name = 'home.html'
        context_object_name = 'all_module_list'

class ModuleList(APIView):
        def get(self,request):
                module1=Module.objects.all()
                serializer= ModuleSerializer(module1,many=True)
                return Response(serializer.data)

        def post(self):
                pass

