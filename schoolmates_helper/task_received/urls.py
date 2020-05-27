from django.urls import path
from . import views

app_name = 'task_received'
urlpatterns = [
    path('', views.index, name='index'),
    path('all_task_received/', views.all_task_received, name='all_task_received'),
    path('<int:task_id>/task_revoke/', views.task_revoke, name='task_revoke'),
    path('<int:task_id>/task_revoke/reasons/', views.reasons_revoke, name='reasons_revoke'),
    path('<int:task_id>/task_detail', views.task_detail, name='task_detail'),
    path('<int:task_id>/task_finished', views.task_finished, name='task_finished'),
    path('all_task_received/<int:tasktype_id>/', views.task_sometype, name='task_sometype'),
    path('received_tasks_finished/', views.received_tasks_finished, name='received_tasks_finished'),
    path('received_tasks_finished/<int:tasktype_id>/', views.task_sometype_finished, name='task_sometype_finished'),
    path('received_tasks_not_finished/', views.received_tasks_not_finished, name='received_tasks_not_finished'),
    path('received_tasks_not_finished/<int:tasktype_id>', views.task_sometype_not_finished,
         name='task_sometype_not_finished'),
    # 2020年4月25日 swf 新增
    path('comment/',views.comment,name='comment'),
    path('revoke/',views.revoke,name='revoke'),
    # 2020年4月30日 swf 新增
    path('logout/',views.logout,name='logout'),
]
