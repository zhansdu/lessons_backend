from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from . import models
import json

def index(request):
  return render(request,'pages/index.html')

def search(request):
  name = request.GET['name']

  student = models.Student.objects.filter(firstname__contains = name).values()
  context = {
    'name': name,
    'students':student
  }
  return render(request,'pages/search.html',context)

def fullInfo(request):
  students = models.Student.objects.all().values()
  assignments= models.Assignment.objects.all().values()
  context = {
    'students':students,
    'assignments':assignments
  }

  return render(request,'pages/full_info.html',context=context)

def stud_info(request,stud_id):
  student = models.Student.objects.filter(stud_id=stud_id).values()[0]
  stud_grades = models.Grade.objects.filter(stud_id=stud_id)
  grades = []
  for grade in stud_grades:
    grades.append(grade.getAssignmentOfStudent())
  context={
    'student':student,
    'grades':grades
  }
  return render(request,'pages/stud_info.html',context = context)

def update_assignment(request):
  request = json.loads(request.body)
  id = request['id']
  description = request['description']
  assignment = models.Assignment.objects.get(assignment_number=id)
  assignment.description = description
  assignment.save()
  content = {
    'message' : 'Success!',
    'assignment_number' : assignment.assignment_number,
    'assignment_info' : assignment.description
  }
  return JsonResponse(content)