# Generated by Django 3.1.2 on 2021-05-01 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spay', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='friends',
        ),
        migrations.AddField(
            model_name='expense',
            name='friends',
            field=models.ManyToManyField(related_name='friends', to='spay.User'),
        ),
        migrations.RemoveField(
            model_name='expense',
            name='paidBy',
        ),
        migrations.AddField(
            model_name='expense',
            name='paidBy',
            field=models.ManyToManyField(related_name='paid_by', to='spay.User'),
        ),
    ]