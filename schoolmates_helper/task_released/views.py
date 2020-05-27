import os

from django.shortcuts import render
from django.conf import settings
from django.shortcuts import HttpResponse
from App import models
from App.models import Task
from App.models import User
from App.models import TaskType
from App.models import Cancel_reason
from App.models import Contact
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage


@csrf_exempt
def acp(request):
    if request.method == 'GET':
        id2 = request.session['mclass']
        id1 = request.session['user_id']
        user = User.objects.get(pk=id1)
        missions = Task.objects.filter(publisher_id=user)
        paginator = Paginator(missions,12,3)
        try:
            num = request.GET.get('acp', '1')
            number = paginator.page(num)
        except PageNotAnInteger:
            number = paginator.page(1)
        except EmptyPage:
            number = paginator.page(paginator.num_pages)
        context = {
            "missions": paginator,
            "id2": id2,
            "page":number
        }
        return render(request, 'task_released/acp.html', context=context)
    elif request.method == 'POST':
        if request.POST.get('task_type') == "0":
            id2 = 0
        elif request.POST.get('task_type') == "1":
            id2 = 1
        elif request.POST.get('task_type') == "2":
            id2 = 2
        elif request.POST.get('task_type') == "3":
            id2 = 3
        elif request.POST.get('task_type') == "4":
            id2 = 4
        elif request.POST.get('task_type') == "5":
            id2 = 5
        id1 = request.session['user_id']
        request.session['mclass'] = id2
        user = User.objects.get(pk=id1)
        missions = Task.objects.filter(publisher_id=user)
        paginator = Paginator(missions, 12, 3)
        try:
            num = request.POST.get('acp', '1')
            number = paginator.page(num)
        except PageNotAnInteger:
            number = paginator.page(1)
        except EmptyPage:
            number = paginator.page(paginator.num_pages)
        context = {
            "missions": paginator,
            "id2": id2,
            "page": number
        }
        return render(request, 'task_released/acp.html', context=context)


@csrf_exempt
def finish(request):
    if request.method == 'GET':
        id2 = request.session['mclass']
        id1 = request.session['user_id']
        user = User.objects.get(pk=id1)
        missions = Task.objects.filter(publisher_id=user)
        paginator = Paginator(missions,12,3)
        try:
            num = request.GET.get('finish', '1')
            number = paginator.page(num)
        except PageNotAnInteger:
            number = paginator.page(1)
        except EmptyPage:
            number = paginator.page(paginator.num_pages)
        context = {
            "missions": paginator,
            "id2": id2,
            "page":number
        }
        return render(request, 'task_released/finish.html', context=context)
    elif request.method == 'POST':
        if request.POST.get('task_type') == "0":
            id2 = 0
        elif request.POST.get('task_type') == "1":
            id2 = 1
        elif request.POST.get('task_type') == "2":
            id2 = 2
        elif request.POST.get('task_type') == "3":
            id2 = 3
        elif request.POST.get('task_type') == "4":
            id2 = 4
        elif request.POST.get('task_type') == "5":
            id2 = 5
        id1 = request.session['user_id']
        request.session['mclass'] = id2
        user = User.objects.get(pk=id1)
        missions = Task.objects.filter(publisher_id=user)
        paginator = Paginator(missions, 12, 3)
        try:
            num = request.POST.get('finish', '1')
            number = paginator.page(num)
        except PageNotAnInteger:
            number = paginator.page(1)
        except EmptyPage:
            number = paginator.page(paginator.num_pages)
        context = {
            "missions": paginator,
            "id2": id2,
            "page": number
        }
        return render(request, 'task_released/finish.html', context=context)


@csrf_exempt
def un_acp(request):
    if request.method == 'GET':
        id2 = request.session['mclass']
        id1 = request.session['user_id']
        user = User.objects.get(pk=id1)
        missions = Task.objects.filter(publisher_id=user)
        paginator = Paginator(missions,12,3)
        try:
            num = request.GET.get('un_acp', '1')
            number = paginator.page(num)
        except PageNotAnInteger:
            number = paginator.page(1)
        except EmptyPage:
            number = paginator.page(paginator.num_pages)
        context = {
            "missions": paginator,
            "id2": id2,
            "page":number
        }
        return render(request, 'task_released/un_acp.html', context=context)
    elif request.method == 'POST':
        if request.POST.get('task_type') == "0":
            id2 = 0
        elif request.POST.get('task_type') == "1":
            id2 = 1
        elif request.POST.get('task_type') == "2":
            id2 = 2
        elif request.POST.get('task_type') == "3":
            id2 = 3
        elif request.POST.get('task_type') == "4":
            id2 = 4
        elif request.POST.get('task_type') == "5":
            id2 = 5
        id1 = request.session['user_id']
        request.session['mclass'] = id2
        user = User.objects.get(pk=id1)
        missions = Task.objects.filter(publisher_id=user)
        paginator = Paginator(missions, 12, 3)
        try:
            num = request.POST.get('un_acp', '1')
            number = paginator.page(num)
        except PageNotAnInteger:
            number = paginator.page(1)
        except EmptyPage:
            number = paginator.page(paginator.num_pages)
        context = {
            "missions": paginator,
            "id2": id2,
            "page": number
        }
        return render(request, 'task_released/un_acp.html', context=context)


def f_mission(request):

    id1 = request.GET.get("id")
    mission = Task.objects.get(pk=id1)
    mission.is_finished = True
    mission.save()
    request.session['id'] = id1

    return redirect("/task_released/comment/")


@csrf_exempt
def comment(request):
    if request.method == 'GET':
        return render(request, 'task_released/comment.html')
    elif request.method == 'POST':
        comment1 = request.POST.get('comment')
        id1 = request.session.get("id")
        task = Task.objects.get(pk=id1)
        task.comment_for_hunter=comment1
        task.save()
        return render(request, 'task_released/success.html')


def d_mission(request):
    id1 = request.GET.get("id")
    task = Task.objects.get(pk=id1)
    task.is_pickedup = False
    request.session['hunter'] = task.hunter_id
    task.hunter = None
    task.save()
    request.session['id'] = id1
    return redirect("/task_released/reason/")

# 问题：应该就只能一个任务对应一个reason？大概要改一下。
@csrf_exempt
def reason(request):

    if request.method == 'GET':
        return render(request, 'task_released/reason.html')
    elif request.method == 'POST':
        reason = request.POST.get('reason')
        id1 = request.session['id']
        hunter = request.session['hunter']
        cancel = Cancel_reason()
        cancel.cancel_reason = reason
        cancel.task = Task.objects.get(pk=id1)
        cancel.user = User.objects.get(pk=hunter)
        cancel.save()
        return render(request, 'task_released/success.html')


def d_unacpm(request):
    id1 = request.GET.get("id")
    mission = Task.objects.get(pk=id1)
    mission.delete()

    return redirect("/task_released/finish/")


def m_detail(request):
    id1 = request.GET.get("id")
    mission = Task.objects.get(pk=id1)
    type = mission.task_type.typename
    context = {
        "mission": mission,
        "type": type
    }
    return render(request, 'task_released/m_detail.html', context=context)


@csrf_exempt
def m_change(request):
    if request.method == 'GET':
        id1 = request.GET.get("id")
        request.session['id'] = id1
        mission = Task.objects.get(pk=id1)
        type = mission.task_type.typename
        context = {
            "mission": mission,
            "type": type
        }
        return render(request, 'task_released/m_change.html', context=context)
    elif request.method == 'POST':
        id1 = request.session['id']
        Data = request.POST.get('Data')
        m1 = request.POST.get('m1')
        l = request.POST.get('task_type')
        c = request.POST.get('task_contact')
        d = request.POST.get('task_sketch')
        g = request.POST.get('g')
        file = request.FILES.get('task_file')
        destination = open(os.path.join("D:/Schoolmates_Helper/untitled20/static/uploads",file.name),'wb+')
        for chunk in file.chunks():
            destination.write(chunk)
        destination.close()
        mission = Task.objects.get(pk=id1)
        type = TaskType.objects.get(pk=l)
        mission.ddltime = Data
        mission.task_name = m1
        mission.task_type = type
        mission.task_sketch = d
        mission.task_reward = g
        mission.task_file = file.name

        mission.contact_type_publisher = Contact.objects.get(pk=c)
        mission.save()
        return redirect("/task_released/un_acp/")


def download(request):
    name = request.GET.get("name")
    file = open(os.path.join(settings.BASE_DIR,'static','uploads',name),'rb')
    response = HttpResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename ='+name.encode('utf-8').decode('ISO-8859-1')
    return response
