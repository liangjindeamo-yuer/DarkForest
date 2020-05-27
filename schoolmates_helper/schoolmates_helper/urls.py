"""schoolmates_helper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from schoolmates_helper import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('App/', include(('App.urls', 'App'), namespace='App')),
    path('task_square/', include('tasks_square.urls')),
    path('task_received/', include('task_received.urls')),
    path('hunt/', include(('hunt.urls', 'hunt'), namespace='hunt')),
    path('task_released/', include('task_released.urls')),
]
