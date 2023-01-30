from django import forms
from manageApp import models, encrypt


class TeacherLoginForm(forms.Form):
    stuffnum = forms.CharField(label="工号")
    password = forms.CharField(label="密码")

    def clean_stuffnum(self):
        stuffnum = self.cleaned_data.get('stuffnum')
        filter_result = models.TeacherInfo.objects.filter(stuffnum__exact=stuffnum)
        if not filter_result:
            raise forms.ValidationError('用户不存在, 请先注册。')
        return stuffnum

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return encrypt.md5(pwd)
