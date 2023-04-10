from django.contrib import admin
from .models import Student
from .models import Grade
from .models import Assignment

# Register your models here.
admin.site.register(Student)
admin.site.register(Grade)
admin.site.register(Assignment)
