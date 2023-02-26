from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from manageApp import models, forms
from django.db.models import Q
import datetime
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.


def get_article(request):
    if request.method == 'GET':
        page = request.GET.get('page')
        if page:
            page = int(page)
        else:
            page = 1
        queryset = models.ClassInfo.objects.all().order_by('id')
        paginator = Paginator(queryset, 5)
        page_exam_list = paginator.page(page)
        page_num = paginator.num_pages
        if page_exam_list.has_next():
            next_page = page + 1
        else:
            next_page = page
        if page_exam_list.has_previous():
            previous_page = page - 1
        else:
            previous_page = page
        return render(request, 'dividePage.html', {
            'queryset': page_exam_list,
            'page_num': range(1, page_num + 1),
            'curr_page': page,
            'next_page': next_page,
            'previous_page': previous_page
        })


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def register(request):
    if request.method == 'GET':
        form = forms.StudentRegisterForm()
        return render(request, 'register.html', {'form': form})
    if request.method == 'POST':
        form = forms.StudentRegisterForm(data=request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
        return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        if request.POST['mode'] == '教师登录':
            form = forms.TeacherLoginForm(data=request.POST)
            if form.is_valid():
                filter_result = models.TeacherInfo.objects.filter(**form.cleaned_data).first()
                if not filter_result:
                    return render(request, 'teacher.html', {"form": form})
                else:
                    request.session['info'] = {'stuffnum': filter_result.stuffnum}
                    request.session.set_expiry(0)
                    return HttpResponseRedirect('/teacher/')
            return render(request, 'login.html', {"form": form})
        if request.POST['mode'] == '学生登录':
            form = forms.StudentLoginForm(data=request.POST)
            if form.is_valid():
                filter_result = models.StudentInfo.objects.filter(**form.cleaned_data).first()
                if not filter_result:
                    return render(request, 'student.html', {"form": form})
                else:
                    request.session['info'] = {'stunum': filter_result.stunum, 'classnum': filter_result.classnum}
                    request.session.set_expiry(0)
                    return HttpResponseRedirect('/student/')
            return render(request, 'login.html', {"form": form})


def logout(request):
    request.session.clear()
    return HttpResponseRedirect('/login/')


def teacher(request):
    if not request.session.get('info'):
        return HttpResponseRedirect('/login/')
    if request.method == 'GET':
        return render(request, 'teacher.html')


def TeacherExamList(request):
    if request.method == 'GET':
        page = request.GET.get('page')
        if page:
            page = int(page)
        else:
            page = 1
        queryset = models.ExamInfo.objects.all().order_by('id')
        paginator = Paginator(queryset, 5)
        page_exam_list = paginator.page(page)
        page_num = paginator.num_pages
        if page_exam_list.has_next():
            next_page = page + 1
        else:
            next_page = page
        if page_exam_list.has_previous():
            previous_page = page - 1
        else:
            previous_page = page
        return render(request, 'TeacherExamList.html', {
            'queryset': page_exam_list,
            'page_num': range(1, page_num + 1),
            'curr_page': page,
            'next_page': next_page,
            'previous_page': previous_page
        })


def TeacherAddExam(request):
    if request.method == 'GET':
        form = forms.AddExamForm()
        return render(request, 'TeacherAddExam.html', {'form': form})
    if request.method == 'POST':
        form = forms.AddExamForm(data=request.POST)
        if form.is_valid():
            form.save()
            current_exam = models.ExamInfo.objects.latest('id')
            filename = 'E' + str(current_exam.id) + '_answer'
            qset = Q()
            for item in current_exam.pronum.split(','):
                qset |= Q(id=item)
            result = models.ProblemInfo.objects.filter(qset)
            with open('./' + filename + '.txt', 'w', encoding='utf-8') as f:
                i = 1
                for num in result:
                    f.write('第' + str(i) + '题  题号：' + str(num.id) + '\n' + num.answercase + '\n')
                    i += 1
            return HttpResponseRedirect('/teacher/examList/')
        else:
            return render(request, 'TeacherAddExam.html', {'form': form})


def TeacherDeleteExam(request, nid):
    models.ExamInfo.objects.filter(id=nid).delete()
    return HttpResponseRedirect('/teacher/examList/')


def TeacherEditExam(request, nid):
    queryset = models.ExamInfo.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = forms.AddExamForm(instance=queryset)
        return render(request, 'TeacherEditExam.html', {'form': form})
    if request.method == 'POST':
        form = forms.AddExamForm(data=request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            current_exam = models.ExamInfo.objects.filter(id=nid).first()
            filename = 'E' + str(current_exam.id) + '_answer'
            qset = Q()
            for item in current_exam.pronum.split(','):
                qset |= Q(id=item)
            result = models.ProblemInfo.objects.filter(qset)
            with open('./' + filename + '.txt', 'w', encoding='utf-8') as f:
                i = 1
                for num in result:
                    f.write('第' + str(i) + '题  题号：' + str(num.id) + '\n' + num.answercase + '\n')
                    i += 1
            return HttpResponseRedirect('/teacher/examList/')
        else:
            return render(request, 'TeacherEditExam.html', {'form': form})


def TeacherProblemList(request):
    if request.method == 'GET':
        page = request.GET.get('page')
        if page:
            page = int(page)
        else:
            page = 1
        queryset = models.ProblemInfo.objects.all().order_by('id')
        paginator = Paginator(queryset, 5)
        page_exam_list = paginator.page(page)
        page_num = paginator.num_pages
        if page_exam_list.has_next():
            next_page = page + 1
        else:
            next_page = page
        if page_exam_list.has_previous():
            previous_page = page - 1
        else:
            previous_page = page
        return render(request, 'TeacherProblemList.html', {
            'queryset': page_exam_list,
            'page_num': range(1, page_num + 1),
            'curr_page': page,
            'next_page': next_page,
            'previous_page': previous_page
        })



def TeacherDeleteProblem(request, nid):
    if request.method == 'GET':
        models.ProblemInfo.objects.filter(id=nid).delete()
        return HttpResponseRedirect('/teacher/ProblemList/')


def TeacherEditProblem(request, nid):
    queryset = models.ProblemInfo.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = forms.AddProblemForm(instance=queryset)
        return render(request, 'TeacherEditProblem.html', {'form': form})
    if request.method == 'POST':
        form = forms.AddProblemForm(data=request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teacher/ProblemList/')
        else:
            return render(request, 'TeacherEditProblem.html', {'form': form})


def TeacherAddProblem(request):
    if request.method == 'GET':
        form = forms.AddProblemForm()
        return render(request, 'TeacherAddProblem.html', {'form': form})
    if request.method == 'POST':
        form = forms.AddProblemForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teacher/ProblemList/')
        else:
            return render(request, 'TeacherAddProblem.html', {'form': form})


def TeacherClassList(request):
    if request.method == 'GET':
        page = request.GET.get('page')
        if page:
            page = int(page)
        else:
            page = 1
        stuffnum = request.session['info']['stuffnum']
        queryset = models.ClassInfo.objects.filter(teacher=stuffnum).order_by('id')
        paginator = Paginator(queryset, 5)
        page_exam_list = paginator.page(page)
        page_num = paginator.num_pages
        if page_exam_list.has_next():
            next_page = page + 1
        else:
            next_page = page
        if page_exam_list.has_previous():
            previous_page = page - 1
        else:
            previous_page = page
        return render(request, 'TeacherClassList.html', {
            'queryset': page_exam_list,
            'page_num': range(1, page_num + 1),
            'curr_page': page,
            'next_page': next_page,
            'previous_page': previous_page
        })


def TeacherAddClass(request):
    stuffnum = request.session['info']['stuffnum']
    if request.method == 'GET':
        form = forms.AddClassForm()
        return render(request, 'TeacherAddClass.html', {'form': form, 'stuffnum': stuffnum})
    if request.method == 'POST':
        form = forms.AddClassForm(data=request.POST)
        if form.is_valid():
            form.save()
            current_teacher = models.TeacherInfo.objects.filter(stuffnum=stuffnum)
            classid = models.ClassInfo.objects.filter(classname=request.POST['classname']).first().id
            current_teacher.update(classnum=current_teacher.first().classnum + ',' + str(classid))
            return HttpResponseRedirect('/teacher/classList/')
        else:
            return render(request, 'TeacherAddClass.html', {'form': form})


def TeacherDeleteClass(request, nid):
    if request.method == 'GET':
        models.ClassInfo.objects.filter(id=nid).delete()
        return HttpResponseRedirect('/teacher/classList/')


def TeacherStudentList(request):
    if request.method == 'GET':
        page = request.GET.get('page')
        selected_class = request.GET.get('class')
        if page:
            page = int(page)
        else:
            page = 1
        if selected_class:
            selected_class = int(selected_class)
        stuffnum = request.session['info']['stuffnum']
        classList = models.ClassInfo.objects.filter(teacher=stuffnum)
        queryset = models.StudentInfo.objects.filter(classnum=selected_class).order_by('id')
        paginator = Paginator(queryset, 5)
        page_exam_list = paginator.page(page)
        page_num = paginator.num_pages
        if page_exam_list.has_next():
            next_page = page + 1
        else:
            next_page = page
        if page_exam_list.has_previous():
            previous_page = page - 1
        else:
            previous_page = page
        return render(request, 'TeacherStudentList.html', {
            'selected_class': selected_class,
            'class': classList,
            'queryset': page_exam_list,
            'page_num': range(1, page_num + 1),
            'curr_page': page,
            'next_page': next_page,
            'previous_page': previous_page
        })


def TeacherDeleteStudent(request, nid):
    if request.method == 'GET':
        models.StudentInfo.objects.filter(id=nid).delete()
        return HttpResponseRedirect('/teacher/ProblemList/')


def student(request):
    if not request.session.get('info'):
        return HttpResponseRedirect('/login/')
    if request.method == 'GET':
        return render(request, 'student.html')


def StudentExamList(request):
    if request.method == 'GET':
        classnum = request.session['info']['classnum']
        queryset = models.ExamInfo.objects.filter(Q(classnum__contains=classnum+',') |
                                                  Q(classnum__contains=','+classnum))
        now = datetime.datetime.now()
        return render(request, 'StudentExamList.html', {'queryset': queryset, 'date_now': now})


def StudentExam(request, nid):
    exam = models.ExamInfo.objects.filter(id=nid).first()
    if request.method == 'GET':
        qset = Q()
        for item in exam.pronum.split(','):
            qset |= Q(id=item)
        result = models.ProblemInfo.objects.filter(qset)
        return render(request, 'StudentExam.html', {'result': result})
    if request.method == 'POST':

        now_time = timezone.now()
        if exam.endtime < now_time:
            return HttpResponse('考试已结束，提交失败')

        stunum = 'E' + str(nid) + '_' + str(request.session['info']['stunum'])
        with open('./' + stunum + '.txt', 'w', encoding='utf-8') as f:
            i = 0
            for value in request.POST.values():
                if i == 0:
                    i += 1
                    continue
                f.write('第' + str(i) + '题\n' + value + '\n')
                i += 1
        return HttpResponseRedirect('/student/examList/')

