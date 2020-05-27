# author：苏婉芳 2020年5月21日
from django.http import request
from django.test import TestCase, Client
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore

from App.models import *
from django.urls import reverse


# 测试网页返回状态
class WebstatusTest(TestCase):
    # 创建测试数据库
    def create_database(self):
        # 创建User表
        User.objects.create(id=1, username="user1", password=0, repassword=0, is_active=True,
                            email='1@sjtu.edu.cn')
        User.objects.create(id=2, username="user2", password=0, repassword=0, is_active=True,
                            email='2@sjtu.edu.cn')
        User.objects.create(id=3, username="user3", password=0, repassword=0, is_active=True,
                            email='3@sjtu.edu.cn')

        # 创建TaskType数据表
        TaskType.objects.create(type_id=1, typesort=1, typename='快递服务')
        TaskType.objects.create(type_id=2, typesort=2, typename='修理服务')
        TaskType.objects.create(type_id=3, typesort=3, typename='课后指导')
        TaskType.objects.create(type_id=4, typesort=4, typename='邂逅表白')
        TaskType.objects.create(type_id=5, typesort=5, typename='其他服务')

        # 创建Task表
        # 快递服务类任务
        Task.objects.create(task_name='task1', contact_type_publisher_id=1, publisher_id=1, task_type_id=1,
                            task_time='2020-10-10', task_reward=1,hunter_id=1)
        Task.objects.create(task_name='task2', contact_type_publisher_id=1, publisher_id=1, task_type_id=1,
                            task_time='2020-10-11', task_reward=2)
        Task.objects.create(task_name='task3', contact_type_publisher_id=1, publisher_id=1, task_type_id=1,
                            task_time='2020-10-12', task_reward=3)
        # 其他各类任务
        Task.objects.create(task_name='task4', contact_type_publisher_id=1, publisher_id=1, task_type_id=2,
                            task_time='2020-10-13')
        Task.objects.create(task_name='task5', contact_type_publisher_id=1, publisher_id=1, task_type_id=3,
                            task_time='2020-10-14')
        Task.objects.create(task_name='task6', contact_type_publisher_id=1, publisher_id=1, task_type_id=4,
                            task_time='2020-10-15')
        Task.objects.create(task_name='task6', contact_type_publisher_id=1, publisher_id=1, task_type_id=5,
                            task_time='2020-10-16')

        # contact
        Contact.objects.create(type_id=1,typename='email')
        Contact.objects.create(type_id=2,typename='QQ')
        Contact.objects.create(type_id=3,typename='wechat')
        Contact.objects.create(type_id=4,typename='telephone')
        Contact.objects.create(type_id=5,typename='其它联系方式')

    def test_tasks_received(self):
        self.create_database()
        response = self.client.get('/task_received/all_task_received/1/')
        self.assertEqual(response.status_code, 200)

    def test_task_received_sort(self):
        self.create_database()
        # 未完成
        response = self.client.get('/task_received/received_tasks_not_finished/')
        self.assertEqual(response.status_code, 200)
        # 已完成
        response = self.client.get('/task_received/received_tasks_finished/')
        self.assertEqual(response.status_code, 200)

    def test_task_revoke(self):
        self.create_database()
        # 撤销任务
        response = self.client.get('/task_received/1/task_revoke/reasons/')
        self.assertEqual(response.status_code, 200)

    def test_task_finish(self):
        self.create_database()
        # 完成任务
        response = self.client.get('/task_received/1/task_finished')
        self.assertEqual(response.status_code, 200)

    def test_task_detail(self):
        self.create_database()
        # 任务详情
        c = Client(enforce_csrf_checks=True)
        test_data = {'username': 'user1', 'password': '0'}
        c.post('/hunt/login/', data=test_data)
        response = c.get('/task_received/1/task_detail')
        self.assertEqual(response.status_code, 200)

