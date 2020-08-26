from django.db import models
from django.utils import timezone

# Create your models here.

def getNewDefault():
    return Record.objects.count()+1
    
class Record(models.Model):
    Day = models.IntegerField(unique=True,default= getNewDefault)
    Date = models.DateField(default=timezone.now)
    Exercise1 = models.CharField(max_length=10)
    ML_Course = models.CharField(max_length=10)
    ML_Project = models.CharField(max_length=10)
    Exercise2 = models.CharField(max_length=10)
    DSA_Learning = models.CharField(max_length=10)
    DSA_Coding = models.CharField(max_length=10)
    Walk = models.CharField(max_length=10)
    Problem_Solving = models.CharField(max_length=10)
    
    def __str__(self): 
        return 'Day #'+str(self.Day)