# Create your views here.
from django.shortcuts import render
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

from App.form import User1, Task1
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
import random
from App.models import *


# 任务发布 2020年5月9日 旧版发布不注释掉，每次会发布两个任务
'''def taskup0(request):
    if request.method == 'GET':
        task1 = Task()
        return render(request, 'task.html', locals())
    else:
        task1 = Task()
        task1.task_name = request.POST.get('task_name')
        task_type = request.POST.get('task_type')
        task1.task_reward = request.POST.get('task_reward')
        task1.task_sketch = request.POST.get('task_sketch')
        task1.task_type_id = int(task_type)
        task1.ddltime = request.POST.get('ddltime')
        task1.task_file = request.FILES.get('task_file')
        user_id = request.session.get('user_id')
        task1.publisher_id = user_id
        task1.save()
        return HttpResponse('发布成功')'''


# 新版任务发布，以这个为准，之前的先不删了，对应的前端是task_form.html
def task_up(request):
    if request.method == 'GET':
        task1 = Task1()
        return render(request, 'hunt/task_form.html', locals())
    else:
        task1 = Task1(request.POST, request.FILES)
        if task1.is_valid():
            try:
                user_id = request.session.get('user_id')
                user = User.objects.get(pk=user_id)
                contactid = request.POST.get('contact_type_publisher')
                contactname = Contact.objects.get(pk=contactid).typename

                task1.cleaned_data['publisher_id'] = user_id
                if getattr(user, contactname) == None:
                #return render(request, 'hunt/task_form.html', locals())
                    return render(request, 'hunt/task_nocontact.html', context={'task': task1,
                                                                      'contactname': contactname, })
            except:
                return render(request, 'hunt/no login.html')

            else:
                Task.objects.create(**task1.cleaned_data)
                return render(request, 'hunt/task_up_successfully.html', locals())
        else:
            return render(request, 'hunt/task_form.html', locals())



def taskcopy(request):
    taskid0 = request.session.get('task_id')
    task = Task.objects.filter(task_id=taskid0)
    task.publisher_id = request.session.get('user_id')
    task.save()


@csrf_exempt # 用户登录
def login(request):
    if request.method == 'GET':
        data = {
            'title': '登录',
        }
        return render(request, 'hunt/login.html', context=data)
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = User.objects.filter(Q(username=username) | Q(email=username))
        if users.exists():
            users = users.filter(password=password)
            if users.exists():
                user1 = users.first()
                user1.is_active = True

                user1.save()  # 登录状态修改
                request.session['username'] = user1.username
                request.session['user_id'] = user1.id
                # swf:第二轮之后实现，显示登录成功后几秒自动跳转到任务广场，现在先:直接到任务广场APP的视图
                return HttpResponseRedirect(reverse('tasks_square:task_square'))
                #return HttpResponse('发布成功')
            else:
                print('密码错误')
                return HttpResponse('密码错误')
        print('用户名不存在')
        return HttpResponse('用户名不存在')


# 注册
def index(request):
    if request.method == 'GET':
        user1 = User1()
        return render(request, 'hunt/data_form.html', locals())
    else:
        user1 = User1(request.POST, request.FILES)
        if user1.is_valid():

            user1.save()
            return render(request, 'hunt/logon_successfully.html')

        else:
            return render(request, 'hunt/data_form.html', locals())


# 个人信息显示与修改
def edit0(request):

    alphabet = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()'
    character = random.sample(alphabet, 5)
    characters=character[0]+character[1]+character[2]+character[3]+character[4]

    try:
        user_id = request.session.get('user_id')



        user = User.objects.get(id=user_id)
        user_name=user.username
        email0 =user.email
        if request.method == "POST":
        # 注意：这里由于用户名邮箱设置不能重名,所以这里的方法是调用修改后先把他改成一个其他的东西，
        # 这样子如果不修改用户名邮箱，之前的用户名邮箱就会替代这个乱码，这样可能会导致一些问题但目前还没遇到，，
            user.username = characters
            user.email = characters+'1shshhs@sjtu.edu.cn'
            user_form = User1(request.POST, request.FILES)
            user.save()
            Photo=user.icon
            context = {
            'imgs': Photo
        }
            if user_form.is_valid():
                user_cd = user_form.cleaned_data
                user.email = user_cd['email']
                user.tel = user_cd['tel']
                user.username = user_cd['username']
                user.qq = user_cd['qq']
                user.password=user_cd['password']
                user.repassword = user_cd['password']
                user.wechat = user_cd['wechat']
                user.other = user_cd['other']
                user.icon = user_cd['icon']
                user.save()
                return render(request, 'hunt/edit.html', {"user_form": user_form,"user":user})

            else:
                user.username=user_name
                user.email=email0
                user.save()
                ErrorDict = user_form.errors
                return render(request, 'hunt/edit.html', {"user_form": user_form,"user":user})
        else:

            user_form = User1(instance=user)

            return render(request, 'hunt/edit.html', {"user_form": user_form,"user":user})
    except:
        return render(request, 'hunt/no login.html')

