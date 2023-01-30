from django.db import models

# Create your models here.


class StudentInfo(models.Model):
    school = models.CharField(verbose_name='学校', max_length=16)
    stunum = models.IntegerField(verbose_name='学号')
    name = models.CharField(verbose_name='姓名', max_length=16)
    password = models.CharField(verbose_name='密码', max_length=64)
    classnum = models.IntegerField(verbose_name='班级编号')


class TeacherInfo(models.Model):
    school = models.CharField(verbose_name='学校', max_length=16)
    stuffnum = models.IntegerField(verbose_name='工号')
    name = models.CharField(verbose_name='姓名', max_length=16)
    password = models.CharField(verbose_name='密码', max_length=64)
    classnum = models.IntegerField(verbose_name='班级编号')


class ExamInfo(models.Model):
    name = models.CharField(verbose_name='学校', max_length=16)
    sttime = models.DateTimeField()
    endtime = models.DateTimeField()
    pronum = models.CharField(verbose_name='题目编号', max_length=128)
    classnum = models.CharField(verbose_name='班级编号', max_length=128)
