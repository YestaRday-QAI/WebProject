from django.contrib import admin
from manageApp import models

# Register your models here.

admin.site.register(models.TeacherInfo)
admin.site.register(models.StudentInfo)
admin.site.register(models.ExamInfo)
admin.site.register(models.ProblemInfo)
admin.site.register(models.ClassInfo)

