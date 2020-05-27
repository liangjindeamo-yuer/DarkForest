from django.urls import path

from . import views

app_name = 'hunt'
urlpatterns = [

    path('logon/', views.index, name='index'),
    #注册,
    path('login/',views.login,name='login'),
    #登录
    path('edit',views.edit0,name='edit'),
    #个人信息修改
    path('up0/',views.task_up,name='up0'),
    #任务发布
    # path('up1/', views.taskup0, name='up1')
    ]