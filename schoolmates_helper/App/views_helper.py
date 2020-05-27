# _*_ coding: utf-8 _*_
# 开发团队：软件工程第5组
# 开发人员：莨瑾
# 开发时间：2020/3/21 16:32
# 文件名称: views_helper.py
# 开发工具：PyCharm
from django.core.mail import send_mail
from django.template import loader

from App.models import User
from schoolmates_helper.settings import *


def send_email_activate(username,receive,u_token):
    subject = 'SchoolHelper_activation'
    message = '<h1>Hello<h1>'
    from_email = EMAIL_HOST_USER
    recipient_list = [receive,]
    data = {
         'username':  username,
         'activate_url': 'http://'+SERVER_NAME+'/App/activate/?u_token='+u_token
    }
    html_message =loader.get_template('user/activate.html').render(data)
    send_mail(subject=subject,message=message,html_message=html_message,from_email=from_email,recipient_list=recipient_list)

def send_email_receive(username_publisher,username_hunter,task_id,task_name,receive,email,contact_way):
    subject = 'SchoolHelper_团队'
    message = '<h1>Hello<h1>'
    from_email = EMAIL_HOST_USER
    recipient_list = [receive,]
    data = {
        'username_hunter':username_hunter,
        'username_publisher':username_publisher,
        'task_id':task_id,
        'task_name':task_name,
        'email':email,
        'contact_way':contact_way,
    }
    html_message =loader.get_template('user/receive.html').render(data)
    send_mail(subject=subject,message=message,html_message=html_message,from_email=from_email,recipient_list=recipient_list)
def send_email_relieve(username_publisher,username_hunter,task_id,task_name,receive,reason):
    subject = 'SchoolHelper_团队'
    message = '<h1>Hello<h1>'
    from_email = EMAIL_HOST_USER
    recipient_list = [receive,]
    data = {
        'username_hunter':username_hunter,
        'username_publisher':username_publisher,
        'task_id':task_id,
        'task_name':task_name,
        'reason':reason,
    }
    html_message =loader.get_template('user/relieve.html').render(data)
    send_mail(subject=subject,message=message,html_message=html_message,from_email=from_email,recipient_list=recipient_list)
def send_email_relieve2(username_publisher,username_hunter,task_id,task_name,receive,reason):
    subject = 'SchoolHelper_团队'
    message = '<h1>Hello<h1>'
    from_email = EMAIL_HOST_USER
    recipient_list = [receive,]
    data = {
        'username_hunter':username_hunter,
        'username_publisher':username_publisher,
        'task_id':task_id,
        'task_name':task_name,
        'reason':reason,
    }
    html_message =loader.get_template('user/relieve2.html').render(data)
    send_mail(subject=subject,message=message,html_message=html_message,from_email=from_email,recipient_list=recipient_list)
def send_email_finish(username_publisher,username_hunter,task_id,task_name,receive):
    subject = 'SchoolHelper_团队'
    message = '<h1>Hello<h1>'
    from_email = EMAIL_HOST_USER
    recipient_list = [receive,]
    data = {
        'username_hunter':username_hunter,
        'username_publisher':username_publisher,
        'task_id':task_id,
        'task_name':task_name,
    }
    html_message =loader.get_template('user/finish.html').render(data)
    send_mail(subject=subject,message=message,html_message=html_message,from_email=from_email,recipient_list=recipient_list)


def is_activated(user_id):
    user = User.objects.get(pk=user_id)
    if user.is_active:
        return True
    else:
        return False
