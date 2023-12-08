from django.db import models

# Create your models here.
class Dept(models.Model):
    Dept_no=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    Loc=models.CharField(max_length=200)

class Emp(models.Model):
    Emp_no=models.IntegerField(primary_key=True)
    Ename=models.CharField(max_length=100) 
    job=models.CharField(max_length=100)
    Mgr=models.IntegerField()
    Hiredate=models.DateField()
    com=models.IntegerField()
    Dept_no=models.OneToOneField(Dept,on_delete=models.CASCADE)

class Salgrade(models.Model):
    Grade=models.IntegerField(primary_key=True)
    Losal=models.IntegerField()
    Hisal=models.IntegerField()