from django.db import models
#from django.contrib.auth.models import AbstractUser
# Create your models here.
class Professor(models.Model):
        professor_id = models.CharField(primary_key=True,unique=True,max_length=6)
        name = models.CharField(max_length=20)
        def __str__(self):
                return self.professor_id+' '+self.name

class Module(models.Model):
        module_id = models.CharField(max_length=6,unique=True,primary_key=True)
        name = models.CharField(max_length=30)
        def __str__(self):
                return self.module_id+' '+self.name

class ModuleInstance(models.Model):
        module= models.ForeignKey(Module,on_delete=models.CASCADE)
        year = models.IntegerField()
        semester = models.IntegerField()
        professor = models.ManyToManyField(Professor)
        class Meta:
                unique_together=(("year","semester","module"),)
        def __str__(self):
                return self.module.module_id+' '+self.module.name+' Year '+str(self.year)+' Semester '+str(self.semester)

class Rating(models.Model):
        professor = models.ForeignKey(Professor,on_delete=models.CASCADE)
        moduleInstance = models.ForeignKey('ModuleInstance',on_delete=models.CASCADE)
        rating = models.IntegerField()
        def __str__(self):
                return self.moduleInstance.module.module_id+' '+self.moduleInstance.module.name+' Year '+str(self.moduleInstance.year)+' Semester '\
                +str(self.moduleInstance.semester)+' / '+self.professor.professor_id+' '+self.professor.name+' / rating '+str(self.rating)
'''
class CustomUser(AbstractUser):
        email= models.CharField(max_length=20)
'''

