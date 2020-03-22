from django.urls import path
from .views import HomePageView,GetModule,ModuleList,ProfessorList,SpecificRating,RateProfessor,Register,Login

urlpatterns = [
        path('',HomePageView.as_view(), name='home'),
        path('hello/',GetModule, name='hello'),
        path('module/',ModuleList.as_view(), name='modulelist'),
        path('view/',ProfessorList.as_view(), name='professorlist'),
        path('average/',SpecificRating.as_view(), name='average'),
        path('rate/',RateProfessor.as_view(), name='rate'),
        path('register/',Register, name='register'),
        path('login/',Login, name='login'),
]
