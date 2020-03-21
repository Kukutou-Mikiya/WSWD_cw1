from django.urls import path
from .views import HomePageView,GetModule,ModuleList,ProfessorList

urlpatterns = [
        path('',HomePageView.as_view(), name='home'),
        path('hello/',GetModule, name='hello'),
        path('module/',ModuleList.as_view(), name='modulelist'),
        path('view/',ProfessorList.as_view(), name='professorlist'),
]