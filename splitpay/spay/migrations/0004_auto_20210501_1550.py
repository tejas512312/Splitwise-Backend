# Generated by Django 3.2 on 2021-05-01 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spay', '0003_auto_20210501_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='users',
        ),
        migrations.RemoveField(
            model_name='group',
            name='users',
        ),
        migrations.AddField(
            model_name='expense',
            name='friends',
            field=models.ManyToManyField(related_name='friends', to='spay.User'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(to='spay.Group'),
        ),
        migrations.RemoveField(
            model_name='expense',
            name='group',
        ),
        migrations.AddField(
            model_name='expense',
            name='group',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='group', to='spay.group'),
        ),
    ]