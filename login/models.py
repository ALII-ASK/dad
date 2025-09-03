from django.db import models

class Teacher(models.Model):
    teacher_id=models.IntegerField(primary_key=True)
    firstname=models.CharField(max_length=40)
    lastname=models.CharField(max_length=40)
   
class Subject(models.Model):
    subject_id=models.IntegerField(primary_key=True)
    subject_name=models.CharField(max_length=200)
   

class Detail(models.Model):
    detail_id=models.IntegerField(primary_key=True)
    detail=models.TextField(null=True)
  