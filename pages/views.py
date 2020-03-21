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
                rateList=[]
                professors=Professor.objects.all()
                for professor in professors:
                        data = {'name':professor.name}
                        data['id']=professor.professor_id
                        rates = Rating.objects.filter(professor=professor)
                        sum=0
                        if rates.count()!=0:
                                for rate in rates:
                                        sum+=rate.rating
                                average = sum/len(rates)
                        else:
                                average = 0
                        data['rating'] = average
                        rateList.append(data)
                #rua=serializer.data
                #rua['rating']=
                return Response(rateList)

        def post(self):
                pass