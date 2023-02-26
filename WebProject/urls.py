"""WebProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from manageApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),

    # 分页组件
    path('divpage/', views.get_article),
    # 教师页面
    path('teacher/', views.teacher),
    # 考试
    path('teacher/examList/', views.TeacherExamList),
    path('teacher/addExam/', views.TeacherAddExam),
    path('teacher/<int:nid>/deleteExam/', views.TeacherDeleteExam),
    path('teacher/<int:nid>/editExam/', views.TeacherEditExam),
    # 题库
    path('teacher/ProblemList/', views.TeacherProblemList),
    path('teacher/AddProblem/', views.TeacherAddProblem),
    path('teacher/<int:nid>/DeleteProblem/', views.TeacherDeleteProblem),
    path('teacher/<int:nid>/EditProblem/', views.TeacherEditProblem),
    # 班级
    path('teacher/classList/', views.TeacherClassList),
    path('teacher/addClass/', views.TeacherAddClass),
    path('teacher/<int:nid>/deleteClass/', views.TeacherDeleteClass),
    path('teacher/studentList/', views.TeacherStudentList),
    path('teacher/<int:nid>/deleteStudent/', views.TeacherDeleteStudent),

    # 学生页面
    path('student/', views.student),
    path('student/examList/', views.StudentExamList),
    path('student/<int:nid>/exam/', views.StudentExam),
]
