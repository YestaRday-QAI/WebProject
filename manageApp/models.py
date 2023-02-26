from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

# Create your models here.


class StudentInfo(models.Model):
    school = models.CharField(verbose_name='学校', max_length=16)
    stunum = models.IntegerField(verbose_name='学号')
    name = models.CharField(verbose_name='姓名', max_length=16)
    password = models.CharField(verbose_name='密码', max_length=128)
    classnum = models.CharField(verbose_name='班级编号', max_length=64)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.password = make_password(self.password)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)


class TeacherInfo(models.Model):
    school = models.CharField(verbose_name='学校', max_length=16)
    stuffnum = models.IntegerField(verbose_name='工号')
    name = models.CharField(verbose_name='姓名', max_length=16)
    password = models.CharField(verbose_name='密码', max_length=128)
    classnum = models.CharField(verbose_name='班级编号', max_length=64)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.password = make_password(self.password)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)


class ExamInfo(models.Model):
    name = models.CharField(verbose_name='考试名称', max_length=16)
    sttime = models.DateTimeField(verbose_name='开始时间')
    endtime = models.DateTimeField(verbose_name='结束时间')
    pronum = models.CharField(verbose_name='题目编号', max_length=256)
    classnum = models.CharField(verbose_name='班级编号', max_length=64)


# class ProgramProblemInfo(models.Model):
#     pronum = models.CharField(verbose_name='题目编号', max_length=16)
#     name = models.CharField(verbose_name='题目名称', max_length=16, default='problem')
#     content = models.TextField(verbose_name='题目内容', blank=True, null=True)
#     case = models.TextField(verbose_name='测试用例', blank=True, null=True)


class ProblemInfo(models.Model):
    problemType = (
        (1, '编程题'),
        (2, '选择题'),
        (3, '填空题'),
        (4, '判断题'),
    )
    type = models.SmallIntegerField(verbose_name='题目类型', choices=problemType)
    name = models.CharField(verbose_name='题目名称', max_length=16, blank=True, null=True)
    content = models.TextField(verbose_name='题目内容', blank=True, null=True)
    answercase = models.TextField(verbose_name='答案示例', blank=True, null=True)


class ClassInfo(models.Model):
    teacher = models.IntegerField(verbose_name='教师工号')
    classname = models.CharField(verbose_name='班级名称', max_length=32)
    coursename = models.CharField(verbose_name='课程名称', max_length=32)