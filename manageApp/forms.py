from django import forms
from manageApp import models
from django.contrib.auth.hashers import check_password


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
        stuffnum = self.cleaned_data.get('stuffnum')
        password = self.cleaned_data.get('password')
        filter_result = models.TeacherInfo.objects.filter(stuffnum__exact=stuffnum).first()
        if not check_password(password, filter_result.password):
            raise forms.ValidationError('工号或密码错误')
        return filter_result.password


class StudentLoginForm(forms.Form):
    stunum = forms.CharField(label="学号")
    password = forms.CharField(label="密码")

    def clean_stunum(self):
        stunum = self.cleaned_data.get('stunum')
        filter_result = models.StudentInfo.objects.filter(stunum__exact=stunum)
        if not filter_result:
            raise forms.ValidationError('用户不存在, 请先注册。')
        return stunum

    def clean_password(self):
        stunum = self.cleaned_data.get('stunum')
        password = self.cleaned_data.get('password')
        filter_result = models.StudentInfo.objects.filter(stunum__exact=stunum).first()
        if not stunum and check_password(password, filter_result.password):
            raise forms.ValidationError('学号或密码错误')
        return filter_result.password


class StudentRegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(label="密码", widget=forms.PasswordInput)

    class Meta:
        model = models.StudentInfo
        fields = ['school', 'stunum', 'name', 'password', 'classnum']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 4:
            raise forms.ValidationError('您的密码应大于6位。')
        elif len(password) > 16:
            raise forms.ValidationError('您的密码应小于16位。')
        return password

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('密码不匹配，请重新输入。')
        return confirm_password


class AddExamForm(forms.ModelForm):
    class Meta:
        model = models.ExamInfo
        fields = '__all__'
        widgets = {
            'sttime': forms.DateTimeInput(attrs={'type': "datetime-local"}),
            'endtime': forms.DateTimeInput(attrs={'type': "datetime-local"}),
        }

    def clean_endtime(self):
        sttime = self.cleaned_data.get('sttime')
        endtime = self.cleaned_data.get('endtime')
        if sttime and endtime and sttime > endtime:
            raise forms.ValidationError('开始时间应早于结束时间')
        return endtime


class AddProblemForm(forms.ModelForm):
    class Meta:
        model = models.ProblemInfo
        fields = '__all__'


class AddClassForm(forms.ModelForm):
    class Meta:
        model = models.ClassInfo
        fields = '__all__'
