from django.test import TestCase,Client
from App.models import User,Task,TaskType,Contact
# Create your tests here.
class ModelTest(TestCase):
    def setUp(self):
        User.objects.create(id=1, username="tester",email="1@sjtu.edu.cn",password='1',repassword='1',tel=0)
        Task.objects.create(id=1,task_name="test",task_reward=1)
        self.login_user = {'username':'tester','password':'1'}
        #验证登录成功了吗
        #response = self.client.post('hunt/login/',data=self.login_user)
        #self.assertEqual(response.status_code, 200)
        c= Client()
        user=User.objects.get(username="tester")
        self.assertEqual(user.username, "tester")

    def test_login_action_username_password_null(self):
        '''用户密码为空'''
        test_data = {'username': '', 'password': ''}
        response = self.client.post('/hunt/login/', data=test_data)
        self.assertEqual(response.status_code, 200)
        #self.assertIn(b"username or password error!", response.content)

    def test_login_action_username_password_error(self):
        '''用户名密码错误'''
        test_data = {'username': 'tester', 'password': '123'}
        response = self.client.post('/hunt/logon/', data=test_data)
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/hunt/login/', data=test_data)
        self.assertEqual(response.status_code, 200)


    def test_login_action_success(self):
        '''测试登陆成功'''
        test_data = {'username': 'tester', 'password': '1'}
        response = self.client.post('/hunt/login/', data=test_data)
        self.assertEqual(response.status_code, 302)

        #验证资料修改
        test_data = {'username': 'teste1r', 'password': '1'}
        response = self.client.post('/hunt/edit', data=test_data)
        self.assertEqual(response.status_code, 200)
    def test_user_models(self):
        result = User.objects.get(username="tester")
        #用户信息否一致
        self.assertEqual(result.tel,0)
    def test_task_up(self):
        '''测试发布成功'''
        test_data = {'task_name': 'test','task_reward':1}
        response = self.client.post('/hunt/up0/', data=test_data)
        self.assertEqual(response.status_code, 200)

    def test_task_models(self):
        result = Task.objects.get(task_name="test")
        self.assertEqual(result.task_reward, 1)

