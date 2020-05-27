# _*_ coding: utf-8 _*_
# 开发团队：软件工程第5组
# 开发人员：莨瑾
# 开发时间：2020/3/20 16:15
# 文件名称: urls.py
# 开发工具：PyCharm
from django.urls import path

from App import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('alltask/', views.alltask, name='alltask'),
    path('alltaskwithparams/<int:typeid>', views.alltask_with_params, name='alltask_with_params'),
    path('alltasksort/<int:typeid>/<slug:typesort1>/<slug:typesort2>/<slug:typesort3>', views.alltask_sort,
         name='alltask_sort'),

    path('task/', views.task, name='task'),
    path('mine/', views.mine, name='mine'),

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('checkuser/', views.checkuser, name='checkuser'),
    path('checkemail/', views.checkemail, name='checkemail'),
    path('checklogin/', views.checklogin, name='checklogin'),

    path('logout/', views.logout, name='logout'),

    path('activate/', views.activate, name='activate'),

    path('sendemail/', views.sendemail, name='send_email'),

    path('receivetask/', views.receivetask, name='receivetask'),
    path('relievetask/', views.relievetask, name='relievetask'),
    path('relievetask2/', views.relievetask2, name='relievetask2'),
    path('finishtask/', views.finishtask, name='finishtask'),

    path('aboutus/', views.aboutus, name='aboutus'),
    path('callus/', views.callus, name='callus'),

    path('alltaskpublisher/', views.alltaskpublisher, name='alltaskpublisher'),
    path('alltaskpublisherwithparams/<int:typeid>/', views.alltaskpublisher_with_params,
         name='alltaskpublisher_with_params'),
    path('alltaskpublishersort/<int:typeid>/<int:sort_way>/',
         views.alltaskpublisher_sort, name='alltaskpublisher_sort'),

    path('alltaskhunter/', views.alltaskhunter, name='alltaskhunter'),
    path('alltaskhunterwithparams/<int:typeid>/', views.alltaskhunter_with_params,
         name='alltaskhunter_with_params'),
    path('alltaskhuntersort/<int:typeid>/<int:sort_way>/',
         views.alltaskhunter_sort, name='alltaskhunter_sort'),

    path('huntertask/<int:typeid>/<int:sort_way>/', views.huntertask, name='huntertask'),
    path('publishertask/<int:typeid>/<int:sort_way>/', views.publishertask, name='publishertask'),
    path('taskfinished/<int:typeid>/<int:sort_way>/', views.taskfinished, name='taskfinished'),
    path('comment/<int:typeid>/<int:sort_way>/', views.comment, name='comment'),
    path('taskcontent/<int:task_id>/', views.taskcontent, name='taskcontent'),

    path('modifyuser/', views.modifyuser, name='modifyuser'),
    path('modifytask/<int:task_id>/', views.modifytask, name='modifytask'),
]
