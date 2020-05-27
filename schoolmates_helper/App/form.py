from django import forms
from App.models import *
from django.contrib.auth.forms import UserChangeForm
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm


class DateInput(forms.DateInput):
    input_type = 'ddltime'


class Task1(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        # exclude用于禁止模型字段转换表单字段
        exclude = ['is_pickedup', 'hunter', 'reason', 'is_finished', 'comment_hunter', 'comment_publisher',
                   'contact_hunter', 'is_overtime', 'contact_type_hunter']
        labels = {
            'task_name': '任务名',
            'task_file': '相关文件（选填）',
            'task_reward': '任务奖励（必填）',
            'task_sketch': '任务描述（必填）',
            'task_time': '截止时间（必填格式）',
            'task_type': '任务类型',
            'contact_type_publisher': '你希望给出的联系方式'

        }

        error_messages = {
            '__all__': {'required': '请输入',
                        'invalid': '请检查格式'},
            'ddltime': {'required': '请输入截止时间',
                        'invalid': '格式应为2020-09-03'
                        }
        }
        widgets = {
            'task_time': DateInput(),
            'password': forms.PasswordInput(),
            'repassword': forms.PasswordInput()

        }


class Type1(forms.ModelForm):
    class Meta:
        model = TaskType
        fields = '__all__'
        # exclude用于禁止模型字段转换表单字段
        exclude = []
        labels = {

        }

        error_messages = {
            '__all__': {
                'invalid': '请检查格式'},
            'name': {'required': '请输入',
                     'invalid': '请检查格式'
                     }
        }


class User1(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        # exclude用于禁止模型字段转换表单字段
        exclude = ['rank', 'is_active', 'is_delete']
        labels = {
            'username': '用户名',
            'tel': '手机号（选填）',
            'qq': 'QQ（选填）',
            'wechat': '微信（选填）',
            'email': '邮箱',
            'other': '其他信息（选填）',
            'password': '密码',
            'repassword': '再次输入密码',
            'icon': '头像（选填）',
            'photo': '头像'

        }
        widgets = {
            'ddltime': DateInput(),
            'password': forms.PasswordInput(),
            'repassword': forms.PasswordInput()

        }
        error_messages = {
            'username': {'required': '请输入',
                         'invalid': '请检查格式'
                         }
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if "@sjtu.edu.cn" in email:
            return email
        else:
            raise forms.ValidationError("请输入交大邮箱")

    def clean_repassword(self):
        pwd1 = self.cleaned_data.get('password')

        pwd2 = self.cleaned_data.get('repassword')
        p = str(pwd1)
        if pwd1 != pwd2:
            raise forms.ValidationError('密码输入不一致')
        elif len(p) < 6:
            raise forms.ValidationError('密码最短六位')
        else:
            return self.cleaned_data
