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
                            task_time='2020-10-10', task_reward=1)
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

    def test_tasks_squre(self):
        self.create_database()
        response = self.client.get('/task_square/')
        self.assertEqual(response.status_code, 200)

    def test_task_detail(self):
        self.create_database()
        # 任务id=1的任务详情页面
        response = self.client.get('/task_square/1/task_detail/')
        self.assertEqual(response.status_code, 200)
        # 任务id=2的任务详情页面
        response = self.client.get('/task_square/2/task_detail/')
        self.assertEqual(response.status_code, 200)

    def test_task_sort(self):
        self.create_database()
        # 快递服务类——任务分类
        response = self.client.get('/task_square/sort/1/id')
        self.assertEqual(response.status_code, 200)

    def test_task_order(self):
        self.create_database()
        # 全部任务——按酬劳升序
        response = self.client.get('/task_square/sort/0/task_reward')
        self.assertEqual(response.status_code, 200)

    def test_task_sort_order(self):
        self.create_database()
        # 快递服务类任务——按酬劳升序
        response = self.client.get('/task_square/sort/1/id')
        self.assertEqual(response.status_code, 200)

    def test_publisher_detail(self):
        self.create_database()
        # 任务发布者user1——用户详情页面(用户id=1)
        response = self.client.get('/task_square/1/publisher_detail/')
        self.assertEqual(response.status_code, 200)


class ViewsTest(TestCase):
    # 查找任务
    @csrf_exempt  # 客户端提交的post如果不加这段，tests里会出现403error
    def test_findtask(self):
        User.objects.create(id=1, username="user1", password=0, repassword=0, is_active=True,
                            email='1@sjtu.edu.cn')
        Task.objects.create(task_name='taskname', contact_type_publisher_id=1, publisher_id=1, task_type_id=1,
                            task_time='2020-10-10', task_reward=1, pk=1)
        Task.objects.create(task_name='other task', contact_type_publisher_id=1, publisher_id=1, task_type_id=1,
                            task_time='2020-10-10', task_reward=1, pk=2)
        c = Client(enforce_csrf_checks=True)
        response = c.post('/task_square/findtasks/', {'keywords': 'taskname'})
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['tasks'], ['<Task: id=1>'])
        response = c.post('/task_square/findtasks/', {'keywords': 'other'})
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['tasks'], ['<Task: id=2>'])

# swf：2020年5月21日 报错：KeyError: 'sessionid'，无法解决
    @csrf_exempt
    def test_discuss(self):
        User.objects.create(id=1, username="user1", password=0, repassword=0, is_active=True,
                            email='1@sjtu.edu.cn')
        User.objects.create(id=2, username="user2", password=0, repassword=0, is_active=True,
                            email='2@sjtu.edu.cn')
        Task.objects.create(task_name='taskname', contact_type_publisher_id=1, publisher_id=1, task_type_id=1,
                            task_time='2020-10-10', task_reward=1, pk=1)

        # hack the session code to change it to the right one
        c = Client(enforce_csrf_checks=True)
        test_data = {'username': 'user1', 'password': '0'}
        c.post('/hunt/login/', data=test_data)
        '''
        尝试更改缓存session
        session = Session.objects.get(pk=self.client.cookies['sessionid'].value)
        newsession = {'user_id': 2}
        session.session_data = SessionStore().encode(newsession)
        session.save()
        '''
        c.post('/task_square/discuss/1/', {'discussion': '讨论测试用例1'})
        discussion = Discuss.objects.get(task_id=1)
        self.assertEqual(discussion.discuss, '讨论测试用例1')
