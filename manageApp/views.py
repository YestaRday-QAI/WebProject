from django.shortcuts import render

# Create your views here.


def add_exam(request):
    return render(request, 'addExam.html')
