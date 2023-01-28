from django.db import models

# Create your models here.


class StudentInfo(models.Model):
    school = models.CharField(verbose_name='学校', max_length=16)
    stunum = models.IntegerField(verbose_name='学号', max_length=16)
    name = models.CharField(verbose_name='姓名', max_length=16)
    password = models.CharField(verbose_name='密码', max_length=64)
    classnum = models.IntegerField(verbose_name='班级编号', max_length=4)
