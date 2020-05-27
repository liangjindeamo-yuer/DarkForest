# author：苏婉芳

from django.shortcuts import render

from App.models import *
from task_received.models import *
from django.urls import reverse
from django.http import HttpResponseRedirect
# swf:删光models，加这个
from hunt.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# 进入“我接受的任务”按钮
def index(request):
    return render(request, 'task_received/index.html')


# swf 2020年4月30日 改 未登录
def all_task_received(request):
    user_id = request.session.get('user_id')
    task_types = TaskType.objects.all()
    if user_id:
        task_received_list = Task.objects.filter(hunter_id=user_id)
        paginator = Paginator(task_received_list, 5)  # Show 5 contacts per page
        page = request.GET.get('page')
        try:
            task_received_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            task_received_list = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            task_received_list = paginator.page(paginator.num_pages)
        context = {
            'task_types': task_types,
            'task_received_list': task_received_list,
            'user_id': user_id,
        }
        return render(request, 'task_received/all_task_received.html', context)
    else:
        context = {
            'task_types': task_types,
            'task_received_list': None,
            'user_id': None,
        }
        return render(request, 'task_received/all_task_received.html', context)


# ?好像没用到？不敢删
def task_revoke(request, task_id):
    username = request.session.get('username')
    user = User.objects.get(username=username)
    target_task = Task.objects.get(pk=task_id)
    target_task.is_pickedup = False
    target_task.hunter = None
    target_task.contact_type_hunter = None
    target_task.save()
    return HttpResponseRedirect(reverse('task_received:all_task_received'))


def reasons_revoke(request, task_id):
    task = Task.objects.get(pk=task_id)
    request.session['task_id'] = task_id
    return render(request, 'task_received/reasons_revoke.html', context={'task_id': task_id, 'task': task})


# swf 2020年4月25日 新增
def revoke(request):
    reason = Revoke_reason()
    task = Task.objects.get(pk=request.session.get('task_id'))
    reason.task = task
    reason.revoke_reason = request.POST.get('reasons')
    task.is_pickedup = False
    task.hunter_id = None
    task.contact_type_hunter = None
    task.save()
    reason.save()
    return render(request, 'task_received/comment_or_revoke_successfuly.html',
                  context={'task': task, 'comment': 0, 'revoke': 1})


def task_detail(request, task_id):
    username = request.session.get('username')
    user = User.objects.get(username=username)
    task = Task.objects.get(pk=task_id)
    contact = task.contact_type_publisher.typename
    contact = getattr(user, contact)
    return render(request, 'task_received/task_detail.html', context={'task': task,
                                                                      'contact': contact})


# swf：2020年4月25日 改动
def task_finished(request, task_id):
    task = Task.objects.get(pk=task_id)
    request.session['task_id'] = task_id
    return render(request, 'task_received/task_finished', context={'task': task})


# swf：2020年4月25日 新增
def comment(request):
    task = Task.objects.get(pk=request.session.get('task_id'))
    if request.method == 'GET':
        return render(request, 'task_received/task_finished', context={'task': task})
    else:
        username = request.session.get('username')
        user = User.objects.get(username=username)
        task.is_finished = True
        user.rank += 1
        task.comment_for_publisher = request.POST.get('comment')
        task.save()
        return render(request, 'task_received/comment_or_revoke_successfuly.html',
                      context={'task': task, 'comment': 1, 'revoke': 0})


def task_sometype(request, tasktype_id):
    task_types = TaskType.objects.all()
    user_id = request.session.get('user_id')
    tasktype = TaskType.objects.get(pk=tasktype_id)
    if user_id:
        tasklist_sometype = Task.objects.filter(task_type=tasktype, hunter_id=user_id)
        paginator = Paginator(tasklist_sometype, 5)  # Show 5 contacts per page
        page = request.GET.get('page')
        try:
            tasklist_sometype = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            tasklist_sometype = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            tasklist_sometype = paginator.page(paginator.num_pages)
        return render(request, 'task_received/tasks_sometype.html',
                      context={
                          'tasklist_sometype': tasklist_sometype,
                          'task_types': task_types,
                          'typeid_now': tasktype_id
                      }
                      )
    else:
        tasklist_sometype = Task.objects.filter(task_type=tasktype, hunter_id=user_id)
        return render(request, 'task_received/tasks_sometype.html',
               context={
                   'tasklist_sometype': tasklist_sometype,
                   'task_types': task_types,
                   'typeid_now': tasktype_id,
               }
               )


def task_sometype_finished(request, tasktype_id):
    username = request.session.get('username')
    user_id = request.session.get('user_id')
    user = User.objects.get(username=username)
    tasktype = TaskType.objects.get(pk=tasktype_id)
    task_types = TaskType.objects.all()
    tasklist_sometype_finished = Task.objects.filter(task_type=tasktype, is_finished=True, hunter_id=user_id)
    paginator = Paginator(tasklist_sometype_finished, 5)  # Show 5 contacts per page
    page = request.GET.get('page')
    try:
        tasklist_sometype_finished = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        tasklist_sometype_finished = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        tasklist_sometype_finished = paginator.page(paginator.num_pages)
    return render(request, 'task_received/task_sometype_finished.html',
                  context={'tasklist_sometype_finished': tasklist_sometype_finished,
                           'task_types': task_types,
                           'typeid_now': tasktype_id})


def task_sometype_not_finished(request, tasktype_id):
    user_id = request.session.get('user_id')
    username = request.session.get('username')
    user = User.objects.get(username=username)
    tasktype = TaskType.objects.get(pk=tasktype_id)
    task_types = TaskType.objects.all()
    # = Task.objects.filter(hunter_id=username,),这里还没有登录，先改成下面这种
    # tasklist_sometype_not_finished = Task.objects.filter(task_type=tasktype, is_finished=False)
    # swf:改 2020年4月17日
    tasklist_sometype_not_finished = Task.objects.filter(task_type=tasktype, is_finished=False, hunter_id=user_id)
    paginator = Paginator(tasklist_sometype_not_finished, 5)  # Show 5 contacts per page
    page = request.GET.get('page')
    try:
        tasklist_sometype_not_finished = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        tasklist_sometype_not_finished = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        tasklist_sometype_not_finished = paginator.page(paginator.num_pages)
    return render(request, 'task_received/task_sometype_not_finished.html',
                  context={'tasklist_sometype_not_finished': tasklist_sometype_not_finished,
                           'task_types': task_types,
                           'typeid_now': tasktype_id})


def received_tasks_finished(request):
    user_id = request.session.get('user_id')
    task_types = TaskType.objects.all()
    if user_id:
        taskslist_received_finished = Task.objects.filter(is_finished=True, hunter_id=user_id)
        paginator = Paginator(taskslist_received_finished, 5)  # Show 5 contacts per page
        page = request.GET.get('page')
        try:
            taskslist_received_finished = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            taskslist_received_finished = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            taskslist_received_finished = paginator.page(paginator.num_pages)
        context = {
            'task_types': task_types,
            'taskslist_received_finished': taskslist_received_finished,
        }
        return render(request, 'task_received/received_tasks_finished.html', context)
    else:
        taskslist_received_finished = Task.objects.filter(is_finished=True)
        context = {
            'task_types': task_types,
            'taskslist_received_finished': taskslist_received_finished,
        }
        return render(request, 'task_received/received_tasks_finished.html', context)


def received_tasks_not_finished(request):
    user_id = request.session.get('user_id')
    task_types = TaskType.objects.all()
    if user_id:
        taskslist_received_not_finished = Task.objects.filter(is_finished=False, hunter_id=user_id)
        paginator = Paginator(taskslist_received_not_finished, 5)  # Show 5 contacts per page
        page = request.GET.get('page')
        try:
            taskslist_received_not_finished = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            taskslist_received_not_finished = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            taskslist_received_not_finished = paginator.page(paginator.num_pages)
        context = {
            'task_types': task_types,
            'taskslist_received_not_finished': taskslist_received_not_finished,
        }
        return render(request, 'task_received/received_tasks_not_finished.html', context)
    else: # 单元测试所用
        taskslist_received_not_finished = Task.objects.filter(is_finished=False)
        context = {
            'task_types': task_types,
            'taskslist_received_not_finished': taskslist_received_not_finished,
        }
        return render(request, 'task_received/received_tasks_not_finished.html', context)


# 退出登录
def logout(request):
    request.session['username'] = None
    request.session['user_id'] = None
    return HttpResponseRedirect(reverse('tasks_square:task_square'))
