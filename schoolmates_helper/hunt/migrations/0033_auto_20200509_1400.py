# Generated by Django 2.0.13 on 2020-05-09 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunt', '0032_auto_20200509_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_file',
            field=models.FileField(blank=True, null=True, upload_to='hunt/static/%Y/%m/%d/'),
        ),
    ]
