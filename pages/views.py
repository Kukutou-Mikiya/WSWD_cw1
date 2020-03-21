from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Module,Professor,Rating
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ModuleSerializer,ProfessorSerializer
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

class ProfessorList(APIView):
        def get(self,request):
                professor1=Professor.objects.all()
                c=0
                for professor in professor1:
                        rates = Rating.objects.filter(professor=professor)
                        sum=0
                        for rate in rates:
                                sum+=rate.rating
                        if sum!=0:
                                sum=sum/len(rates)
                        if c==0:
                                print(professor)
                                c+=1
                serializer= ProfessorSerializer(professor1,many=True)
                #rua=serializer.data
                #rua['rating']=
                return Response(serializer.data)

        def post(self):
                pass