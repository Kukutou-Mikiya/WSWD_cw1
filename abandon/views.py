from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Module,Professor,Rating
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ModuleSerializer,ProfessorSerializer
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def Register(request):
        username=request.GET['username']
        email=request.GET['email']
        password=request.GET['password']
        user=User.objects.create_user(username=username,email=email,password=password)

def Login(request):
        username=request.GET['username']
        password=request.GET['password']
        user = auth.authenticate(username=username,password=password)
        if user:
                auth.login(request,user)
                return HttpResponse('success login')
        else:
                return HttpResponse('failed login')

def Logout(request):
        auth.logout(request)

def GetModule(request):
        return HttpResponse("hello world")

class HomePageView(ListView):
        model = Module
        template_name = 'home.html'
        context_object_name = 'all_module_list'

class ModuleList(APIView):
        def get(self,request):
                module1=Module.objects.all()
                serializer= ModuleSerializer(module1,many=True)
                print(serializer.data)
                return Response(serializer.data)

        def post(self):
                pass

class ProfessorList(APIView):
        def get(self,request):
                #headers=request.data
                print(request.GET)
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
                                average = round(sum/len(rates))
                        else:
                                average = 0
                        data['rating'] = average
                        rateList.append(data)
                #rua=serializer.data
                #rua['rating']=
                return Response(rateList)

        def post(self):
                pass

class SpecificRating(APIView):
        def get(self,request):
                a=request.GET.dict()
                #professor_id=request.GET.get('professor_id')
                #module_id=request.GET.get('module_id')
                professor_id=a['professor_id']
                module_id=a['module_id']
                professor=Professor.objects.filter(professor_id=professor_id)
                module=Module.objects.filter(module_id=module_id)
                rates = Rating.objects.filter(professor=professor[0],module=module[0])
                sum=0
                if rates.count()!=0:
                        for rate in rates:
                                sum+=rate.rating
                        average = round(sum/len(rates))
                else:
                        average = 0
                data = {'rating':average}
                return Response([data])

        def post(self):
                pass

'''
class RateProfessor(APIView):
        def get(self,request):
                professor_id=request.GET['professor_id']
                module_id=request.GET['module_id']
                rating = request.GET['rating']
                semester = request.GET['semester']
                year = request.GET['year']
                module=Module.objects.filter(module_id=module_id,semester=semester,year=year)
                professor=Professor.objects.filter(professor_id=professor_id)
                Rating.objects.create(module=module[0],professor=professor[0],rating=rating)
                return Response()

        def post(self,request):
                pass

'''

@login_required
def RateProfessor(request):
        professor_id=request.GET['professor_id']
        module_id=request.GET['module_id']
        rating = request.GET['rating']
        semester = request.GET['semester']
        year = request.GET['year']
        module=Module.objects.filter(module_id=module_id,semester=semester,year=year)
        professor=Professor.objects.filter(professor_id=professor_id)
        Rating.objects.create(module=module[0],professor=professor[0],rating=rating)
        return HttpResponse('rate success')