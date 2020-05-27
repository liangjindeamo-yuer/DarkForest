# author：苏婉芳
import os

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from App.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def task_square(request):
    user_id = request.session.get('user_id')
    task_types = TaskType.objects.all()

    request.session['mclass'] = 0
    if user_id:
        username = request.session.get('username')
        tasks_list1 = Task.objects.filter(is_pickedup=False, is_overtime=False).exclude(publisher_id=user_id)
        for task in tasks_list1:
            task.soft_delete()
        tasks_list = Task.objects.filter(is_pickedup=False, is_overtime=False).exclude(publisher_id=user_id)
        paginator = Paginator(tasks_list, 9)  # Show 9 contacts per page
        page = request.GET.get('page')
        try:
            tasks = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            tasks = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            tasks = paginator.page(paginator.num_pages)
        data = {
            'tasks_list': tasks_list,
            'task_types': task_types,
            'type_id': 0,
            'username': username,
            'tasks': tasks,
        }
        return render(request, 'tasks_square/task_square.html', context=data)
    # 2020年4月30日 swf 新增 用户未登录时也可看广场
    else:
        tasks_list1 = Task.objects.filter(is_pickedup=False, is_overtime=False)
        for task in tasks_list1:
            task.soft_delete()
        tasks_list = Task.objects.filter(is_pickedup=False, is_overtime=False)
        paginator = Paginator(tasks_list, 9)  # Show 5 contacts per page
        page = request.GET.get('page')
        try:
            tasks = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            tasks = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            tasks = paginator.page(paginator.num_pages)
        data = {
            'tasks_list': tasks_list,
            'task_types': task_types,
            'type_id': 0,
            'username': None,
            'tasks': tasks,
        }
        return render(request, 'tasks_square/task_square.html', context=data)


def task_square_sort(request, type_id, order):
    user_id = request.session.get('user_id')
    username = request.session.get('username')
    task_types = TaskType.objects.all()

    if order == 'task_reward':
        ordername = '按酬劳升序'
    elif order == '-task_reward':
        ordername = '按酬劳降序'
    elif order == 'ddltime':
        ordername = '按截止时间升序'
    elif order == '-ddltime':
        ordername = '按截止时间降序'
    else:
        ordername = '默认排序'

    if type_id != 0:
        sort = TaskType.objects.get(pk=type_id).typename
        if user_id:
            tasks_list1 = Task.objects.filter(is_pickedup=False, task_type=type_id, is_overtime=False).order_by(
                order).exclude(publisher_id=user_id)
            for task in tasks_list1:
                task.soft_delete()
            tasks_list = tasks_list1.filter(is_overtime=False)
        else:
            tasks_list1 = Task.objects.filter(is_pickedup=False, task_type=type_id, is_overtime=False).order_by(order)
            for task in tasks_list1:
                task.soft_delete()
            tasks_list = tasks_list1.filter(is_overtime=False)
    else:
        sort = '全部任务'
        if user_id:
            tasks_list1 = Task.objects.filter(is_pickedup=False, is_overtime=False).order_by(order).exclude(
                publisher_id=user_id)
            for task in tasks_list1:
                task.soft_delete()
            tasks_list = tasks_list1.filter(is_overtime=False)
        else:
            tasks_list1 = Task.objects.filter(is_pickedup=False, is_overtime=False).order_by(order)
            for task in tasks_list1:
                task.soft_delete()
            tasks_list = tasks_list1.filter(is_overtime=False)

    paginator = Paginator(tasks_list, 9)  # Show 5 contacts per page
    page = request.GET.get('page')
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        tasks = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        tasks = paginator.page(paginator.num_pages)

    data = {
        'tasks': tasks,
        'username': username,
        'task_types': task_types,
        'type_id': type_id,
        'sort': sort,
        'ordername': ordername,
    }
    return render(request, 'tasks_square/task_square.html', context=data)


def check_hunt(request, task_id):
    user_id = request.session.get('user_id')
    task = Task.objects.get(pk=task_id)
    if user_id:
        return render(request, 'tasks_square/check_hunt.html', context={'task': task,
                                                                        'user_id': user_id})
    else:
        return render(request, 'tasks_square/check_hunt.html', context={'task': task,
                                                                        'user_id': None})


def hunt_task(request, task_id):
    user_id = request.session.get('user_id')
    user = User.objects.get(pk=user_id)
    contactid = request.POST.get('contacthunter')
    contactname = Contact.objects.get(pk=contactid).typename
    task = Task.objects.get(pk=task_id)
    task.is_pickedup = True
    task.hunter_id = user_id
    task.contact_type_hunter_id = contactid
    if getattr(user, contactname) == None:
        return render(request, 'tasks_square/contacttype.html', context={'task': task,
                                                                         'contactname': contactname, })
    else:
        task.save()
        return render(request, 'tasks_square/hunt_successfully.html', context={'task': task, })


def task_detail(request, task_id):
    task = Task.objects.get(pk=task_id)
    user_id = request.session.get('user_id')
    if user_id:
        data = {
            'task': task,
            'user_id': user_id,
        }
    else:
        data = {
            'task': task,
            'user_id': None,
        }
    return render(request, 'tasks_square/task_detail.html', data)


# swf 2020年4月25日 新增
def publisher_detail(request, publisher_id):
    publisher = User.objects.get(pk=publisher_id)
    his_alltasks = publisher.publisher.all()
    his_finished = publisher.hunter.all()
    return render(request, 'tasks_square/publisher_detail.html',
                  context={'publisher': publisher,
                           'his_alltasks': his_alltasks,
                           'his_finished': his_finished})

@csrf_exempt #客户端提交的post如果不加这段，tests里会出现403error
def findtasks(request):
    keywords = request.POST.get('keywords')
    user_id = request.session.get('user_id')
    task_types = TaskType.objects.all()
    if user_id:
        user = User.objects.get(pk=user_id)
        tasks = Task.objects.all().exclude(publisher_id=user_id)
        finded = []
        for task in tasks:
            if keywords in task.task_name:
                finded.append(task)
            else:
                if task.task_sketch:
                    if keywords in task.task_sketch:
                        finded.append(task)
        data = {
            'tasks': finded,
            'task_types': task_types,
            'type_id': 0,
            'username': user.username,
        }
        return render(request, 'tasks_square/task_square.html', context=data)
    else:
        tasks = Task.objects.all()
        finded = []
        for task in tasks:
            if keywords in task.task_name:
                finded.append(task)
            else:
                if task.task_sketch:
                    if keywords in task.task_sketch:
                        finded.append(task)
        data = {
            'tasks': finded,
            'task_types': task_types,
            'type_id': 0,
            'username': None,
        }
        return render(request, 'tasks_square/task_square.html', context=data)

@csrf_exempt
def discuss(request, task_id):
    user_id = request.session.get('user_id')
    user = User.objects.get(pk=user_id)
    task = Task.objects.get(pk=task_id)
    discussion = Discuss()
    discussion.task = task
    discussion.discuss = request.POST.get('discussion')
    discussion.discussant = user
    discussion.save()
    return HttpResponseRedirect(reverse('tasks_square:task_detail', args=[task_id]))


def response(request, task_id, discussion_id):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(pk=user_id)
        task = Task.objects.get(pk=task_id)
        discussion1 = Discuss.objects.get(pk=discussion_id)
        response1 = Response()
        response1.discuss = discussion1
        response1.response = request.POST.get('response')
        response1.respondent = user
        response1.save()
        return HttpResponseRedirect(reverse('tasks_square:task_detail', args=[task_id]))
    else:
        return render(request, 'tasks_square/task_detail.html')


def delete(request, id, type, task_id):
    if type == 'discuss':
        Discuss.objects.get(pk=id).delete()
    elif type == 'response':
        Response.objects.get(pk=id).delete()
    return HttpResponseRedirect(reverse('tasks_square:task_detail', args=[task_id]))


# 未实现 swf 日期
def download(request, task_id):
    task = Task.objects.get(pk=task_id)
    site = 'static/uploads/'
    name = str(task.task_file)
    site = site + name
    file = open(site, 'rb')
    download_name = name.split("/")[4]
    response = HttpResponse(file)
    response['Content-Type'] = 'application/octet-stream'  # 设置头信息，告诉浏览器这是个文件
    response['Content-Disposition'] = 'attachment;filename=' + download_name.encode('utf-8').decode('ISO-8859-1')
    return response
