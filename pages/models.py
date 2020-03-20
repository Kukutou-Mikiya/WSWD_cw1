from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Professor(models.Model):
        professor_id = models.CharField(primary_key=True,unique=True,max_length=20)
        name = models.CharField(max_length=20)
        def __str__(self):
                return self.professor_id

class Module(models.Model):
        module_id = models.CharField(max_length=20,unique=True)
        year = models.IntegerField()
        semester = models.IntegerField()
        professor = models.ManyToManyField(Professor)
        class Meta:
                unique_together=(("year","semester","module_id"),)
        def __str__(self):
                return self.module_id


class Rating(models.Model):
        professor = models.ForeignKey(Professor,on_delete=models.CASCADE)
        module = models.ForeignKey(Module,on_delete=models.CASCADE)
        rating = models.IntegerField()

class CustomUser(AbstractUser):
        email= models.CharField(max_length=20)

