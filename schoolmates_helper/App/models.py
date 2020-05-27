import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class MainWheel(models.Model):
    img = models.CharField(max_length=255)
    name = models.CharField(max_length=64)
    trackid = models.IntegerField(default=1)

    class Meta:
        db_table = 'smh_wheel'


class User(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=256)
    repassword = models.CharField(max_length=256)
    email = models.EmailField(max_length=30, unique=True)
    icon = models.ImageField(upload_to='icons/%Y/%m/%d/', null=True,default='icons/haha.jpg')
    is_active = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    rank = models.IntegerField(default=0)

    tel = models.PositiveIntegerField(blank=True, null=True)
    qq = models.CharField(max_length=20, blank=True, null=True)
    wechat = models.CharField(max_length=20, blank=True, null=True)
    other = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'smh_user'


class TaskType(models.Model):
    type_id = models.IntegerField(default=1)
    typename = models.CharField(max_length=32)
    typesort = models.IntegerField(default=1)

    class Meta:
        db_table = 'smh_tasktype'


class Contact(models.Model):
    type_id = models.IntegerField(default=0)
    typename = models.CharField(max_length=32)

    class Meta:
        db_table = 'smh_contact_type'


class Task(models.Model):
    contact_type_publisher = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='contact_publisher',
                                               verbose_name='发布人联系方式', db_constraint=False, null=True,blank=True,default=1)
    contact_type_hunter = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='contact_hunter',
                                            verbose_name='委托人联系方式', db_constraint=False, null=True,blank=True)

    task_name = models.CharField(max_length=32)
    task_sketch = models.CharField(max_length=512, null=True,blank=True)
    task_file = models.FileField(upload_to='task_file/%Y/%m/%d/', null=True,blank=True)
    task_type = models.ForeignKey(TaskType, default=1, on_delete=models.SET_DEFAULT)

    task_time = models.DateField(blank=True, null=True)

    task_reward = models.FloatField(default=0, null=True,blank=True)

    is_pickedup = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)
    is_overtime = models.BooleanField(default=False)

    publisher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publisher', verbose_name='发布人',blank=True,null=True)
    hunter = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='hunter', verbose_name='委托人',
                               db_constraint=False, null=True,blank=True)

    comment_publisher = models.CharField(max_length=1000, null=True,blank=True)
    comment_hunter = models.CharField(max_length=1000, null=True, blank=True)

    def removehunter(self):
        self.hunter = None
        self.contact_type_hunter = None

    # 2020年5月16日 swf 软删除过期任务
    # 重写数据库删除方法实现逻辑删除
    def soft_delete(self):
        if self.task_time <= datetime.date.today():
            self.is_overtime = True
            self.save()

    def __str__(self):      # tests.py中查询结果的断言，使用到该函数
        return 'id=%s' % self.pk

    class Meta:
        db_table = 'smh_task'


class Revoke_reason(models.Model):
    revoke_reason = models.CharField(max_length=512, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='revoked_tasks', db_constraint=False)

    class Meta:
        db_table = 'smh_reason'


class Cancel_reason(models.Model):
    cancel_reason = models.CharField(max_length=512, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='canceled_tasks', db_constraint=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_canceled', db_constraint=False)


class Discuss(models.Model):
    discussant = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='discuss_user', verbose_name='评论方',
                                   db_constraint=False, blank=False, null=False)
    discuss = models.CharField(max_length=512, blank=False, null=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='discussed_task')
    discusstime = models.DateTimeField(auto_now_add=True)


class Response(models.Model):
    response = models.CharField(max_length=512, blank=False, null=False)
    discuss = models.ForeignKey(Discuss, on_delete=models.CASCADE, related_name='response_discuss', null=True,
                                db_constraint=False)
    respondent = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='response_user', verbose_name='回复方',
                                   db_constraint=False, blank=False, null=False)
    responsetime = models.DateTimeField(auto_now_add=True)
