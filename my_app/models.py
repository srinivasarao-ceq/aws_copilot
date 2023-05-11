from django.db import models

# Create your models here.
class Student(models.Model):
   stu_id=models.CharField(max_length=10)
   stu_name=models.CharField(max_length=20)
   stu_branch=models.CharField(max_length=10,default="BCA")

   def _str_(self):
      return self.stu_id()

