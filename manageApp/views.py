from django.shortcuts import render, redirect
from manageApp import models, forms
from django.contrib import auth
# Create your views here.


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        form = forms.TeacherLoginForm(data=request.POST)
        if form.is_valid():
            teacher = models.TeacherInfo.objects.filter(**form.cleaned_data).first()
            if not teacher:
                form.add_error('password', '用户名或密码错误')
                return render(request, 'login.html', {"form": form})
        return render(request, 'login.html', {"form": form})


def teacher(request):
    if request.method == 'GET':
        return render(request, 'teacher.html')


def TeacherExamList(request):
    if request.method == 'GET':
        queryset = models.ExamInfo.objects.all()
        return render(request, 'TeacherExamList.html', {'queryset': queryset})


def TeacherAddExam(request):
    if request.method == 'GET':
        return render(request, 'TeacherAddExam.html')
    if request.method == 'POST':
        title = request.POST.get("title")
        stDate = request.POST.get("stDate")
        endDate = request.POST.get("enDate")
        probNum = request.POST.get("probNum")
        classNum = request.POST.get("classNum")
        models.ExamInfo.objects.create(name=title, sttime=stDate, endtime=endDate, pronum=probNum, classnum=classNum)
        return redirect('/teacher/examList/')


def TeacherDeleteExam(request, nid):
    models.ExamInfo.objects.filter(id=nid).delete()
    return redirect('/teacher/examList/')


def TeacherEditExam(request, nid):
    if request.method == 'GET':
        queryset = models.ExamInfo.objects.filter(id=nid).first()
        return render(request, 'TeacherEditExam.html', {'queryset': queryset})
    if request.method == 'POST':
        title = request.POST.get("title")
        stDate = request.POST.get("stDate")
        endDate = request.POST.get("enDate")
        probNum = request.POST.get("probNum")
        classNum = request.POST.get("classNum")
        models.ExamInfo.objects.filter(id=nid).update(name=title, sttime=stDate, endtime=endDate, pronum=probNum,
                                                      classnum=classNum)
        return redirect('/teacher/examList/')

def student(request):
    if request.method == 'GET':
        return render(request, 'student.html')


def StudentExamList(request):
    if request.method == 'GET':
        return render(request, 'StudentExamList.html')
