from django.contrib import admin

# Register your models here.
from App import models

admin.site.register(models.Task)
admin.site.register(models.User)
admin.site.register(models.MainWheel)
admin.site.register(models.TaskType)