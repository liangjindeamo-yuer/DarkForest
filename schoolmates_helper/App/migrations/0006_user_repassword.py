# Generated by Django 2.1.7 on 2020-05-17 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_auto_20200517_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='repassword',
            field=models.CharField(default=0, max_length=256),
            preserve_default=False,
        ),
    ]