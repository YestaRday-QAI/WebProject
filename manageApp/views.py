from django.shortcuts import render

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


def teacher(request):
    if request.method == 'GET':
        return render(request, 'teacher.html')


def student(request):
    if request.method == 'GET':
        return render(request, 'student.html')


def TeacherExamList(request):
    if request.method == 'GET':
        return render(request, 'examList.html')


def TeacherAddExam(request):
    if request.method == 'GET':
        return render(request, 'addExam.html')
