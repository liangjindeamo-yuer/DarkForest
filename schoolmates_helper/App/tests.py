from django.test import TestCase,Client
from App.models import *
import unittest


# Create your tests here.
class ModelTest(TestCase):
    def setUp(self):
        User.objects.create(id=1, username="test1", password="password", email="liangjindeamo@outlook.com",
                            icon='icons/2020/04/18/48A09D141CAFD3F995C448622C2AC65C.jpg', is_active=True,
                            is_delete=False, rank=1, other="github：liangliangliang", qq="2249648511",
                            tel=18272812712, wechat="liang")
        TaskType.objects.create(id=1, type_id=1, typesort=1, typename="快递服务")
        TaskType.objects.create(id=2, type_id=2, typesort=2, typename="修理服务")
        TaskType.objects.create(id=3, type_id=3, typesort=3, typename="课业指导")
        TaskType.objects.create(id=4, type_id=4, typesort=4, typename="邂逅表白")
        TaskType.objects.create(id=5, type_id=5, typesort=5, typename="其他服务")
        Task.objects.create(id=1,task_name="测试用例",task_sketch="这是一个测试罢了",task_type_id=5,
                            task_reward=520,is_pickedup=False,publisher_id=1,is_finished=False,
                            task_time="2020-04-28",contact_type_publisher_id=1)
    #首先测试数据库是否正常运行
    def test_user_models(self):
        result = User.objects.get(username="test1")
        self.assertEqual(result.qq,"2249648511")
        self.assertTrue(result.is_active)

    def test_task_models(self):
        result = Task.objects.get(task_name="测试用例")
        self.assertEqual(result.task_reward,520)
        self.assertFalse(result.is_pickedup)
    def test_tasktype_models_1(self):
        result = TaskType.objects.get(typename="快递服务")
        self.assertEqual(result.id,1)
    def test_tasktype_models_2(self):
        result = TaskType.objects.get(typesort=2)
        self.assertEqual(result.id,2)
    def test_tasktype_models_3(self):
        result = TaskType.objects.get(typesort=3)
        self.assertEqual(result.id,3)
    def test_tasktype_models_4(self):
        result = TaskType.objects.get(typesort=4)
        self.assertEqual(result.id,4)
    def test_tasktype_models_5(self):
        result = TaskType.objects.get(typesort=5)
        self.assertEqual(result.id,5)
    #接着测试网页

    #测试主界面
    def test_mainhome(self):
        self.client=Client()
        response = self.client.get('')
        self.failUnlessEqual(response.status_code, 200)
    #测试手机端初始界面
    def test_home(self):
        self.client=Client()
        response = self.client.get('/App/home/')
        self.failUnlessEqual(response.status_code, 200)
    #测试任务广场界面
    def test_alltask(self):
        self.client=Client()
        response = self.client.get('/App/alltask/')
        self.failUnlessEqual(response.status_code, 200)
    def test_alltaskwithparams(self):
        self.client=Client()
        response = self.client.get('/App/alltaskwithparams/1')
        self.failUnlessEqual(response.status_code, 200)
    def test_alltasksort(self):
        self.client = Client()
        response = self.client.get('/App/alltasksort/1/task_time/task_sketch/id')
        self.failUnlessEqual(response.status_code, 200)
    #测试任务界面
    def test_task(self):
        self.client = Client()
        response = self.client.get('/App/task/')
        self.failUnlessEqual(response.status_code, 200)
    #测试个人主页
    def test_mine(self):
        self.client = Client()
        response = self.client.get('/App/mine/')
        self.failUnlessEqual(response.status_code, 200)
    #测试注册页面
    def test_register(self):
        self.client=Client()
        response = self.client.get('/App/register/')
        self.failUnlessEqual(response.status_code, 200)
    #测试登录界面
    def test_login(self):
        self.client=Client()
        response = self.client.get('/App/login/')
        self.failUnlessEqual(response.status_code, 200)
    #测试界面——关于我们
    def test_aboutus(self):
        self.client=Client()
        response = self.client.get('/App/aboutus/')
        self.failUnlessEqual(response.status_code, 200)
    #测试界面——呼叫客服
    def test_callus(self):
        self.client=Client()
        response = self.client.get('/App/callus/')
        self.failUnlessEqual(response.status_code, 200)
    #测试界面——我发布的所有任务
    def test_alltaskpublisher(self):
        self.client=Client()
        response = self.client.get('/App/alltaskpublisher/')
        self.failUnlessEqual(response.status_code, 200)
    def test_alltaskpublisherwithparams(self):
        self.client=Client()
        response = self.client.get('/App/alltaskpublisherwithparams/1/')
        self.failUnlessEqual(response.status_code, 200)
    def test_alltaskpublishersort(self):
        self.client = Client()
        response = self.client.get('/App/alltaskpublishersort/1/1/')
        self.failUnlessEqual(response.status_code, 200)
    #测试界面——我接受的所有任务
    def test_alltaskhunter(self):
        self.client = Client()
        response = self.client.get('/App/alltaskhunter/')
        self.failUnlessEqual(response.status_code, 200)
    def test_alltaskhunterwithparams(self):
        self.client = Client()
        response = self.client.get('/App/alltaskhunterwithparams/1/')
        self.failUnlessEqual(response.status_code, 200)
    def test_alltaskhuntersort(self):
        self.client = Client()
        response = self.client.get('/App/alltaskhuntersort/1/1/')
        self.failUnlessEqual(response.status_code, 200)
    #测试界面——我接受待完成的任务
    def test_huntertask(self):
        self.client = Client()
        response = self.client.get('/App/huntertask/1/1/')
        self.failUnlessEqual(response.status_code, 200)
    #测试界面——我发布的已被接任务
    def test_publishertask(self):
        self.client = Client()
        response = self.client.get('/App/publishertask/1/1/')
        self.failUnlessEqual(response.status_code, 200)
    #测试界面——已完成的任务
    def test_taskfinished(self):
        self.client = Client()
        response = self.client.get('/App/taskfinished/1/1/')
        self.failUnlessEqual(response.status_code, 200)
    #测试界面——待评价的任务
    def test_comment(self):
        self.client = Client()
        response = self.client.get('/App/comment/1/1/')
        self.failUnlessEqual(response.status_code, 200)
    #测试界面——任务目录
    def test_taskcontent(self):
        self.client = Client()
        response = self.client.get('/App/taskcontent/1/')
        self.failUnlessEqual(response.status_code, 200)


