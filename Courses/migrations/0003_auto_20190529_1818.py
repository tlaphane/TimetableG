# Generated by Django 2.2.1 on 2019-05-29 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0002_auto_20190516_0524'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='Course_Day',
            field=models.CharField(default='Null', max_length=100),
        ),
        migrations.AddField(
            model_name='courses',
            name='Course_Diagonal',
            field=models.CharField(default='Null', max_length=100),
        ),
        migrations.AddField(
            model_name='courses',
            name='Course_Semester',
            field=models.CharField(default='Null', max_length=100),
        ),
        migrations.AddField(
            model_name='courses',
            name='Course_TimeSlot',
            field=models.CharField(default='Null', max_length=100),
        ),
    ]