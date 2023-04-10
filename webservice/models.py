from django.db import models
from datetime import datetime 

class Student(models.Model):
  stud_id = models.IntegerField(primary_key=True,null=False)
  firstname = models.CharField(max_length=255,null=False)
  lastname = models.CharField(max_length=255,null=True)

  def __str__(self):
    return f"{self.stud_id}: {self.firstname} {self.lastname}"


class Assignment(models.Model):
  assignment_number = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255,null=False)
  description = models.CharField(max_length=255,null=True)
  start_date = models.DateField(default=datetime.now)
  due_date = models.DateField(null=True)

  def __str__(self):
    return f"{self.name}"

class Grade(models.Model):
  stud_id = models.ForeignKey(Student,on_delete=models.CASCADE,null=False)
  assignment_number = models.ForeignKey(Assignment,on_delete=models.CASCADE,null=False)
  grade = models.IntegerField(null=False)
  comment = models.TextField(null=True)
  put_date = models.DateField(default=datetime.now)

  def getAssignmentOfStudent(self):
    assignment = Assignment.objects.filter(assignment_number = self.assignment_number.assignment_number)[0]
    
    context = {
      'grade':self.grade,
      'comment':self.comment,
      'assignment': assignment.name,
      'assignment_description':assignment.description
    }

    return context

  def __str__(self):
    return f"{self.stud_id}: {self.assignment_number} - {self.grade}"
