# _*_ coding: utf-8 _*_
# 开发团队：软件工程第5组
# 开发人员：莨瑾
# 开发时间：2020/3/28 19:02
# 文件名称: views.py
# 开发工具：PyCharm
from django.shortcuts import render


def home(request):

    return render(request,'allhome.html')