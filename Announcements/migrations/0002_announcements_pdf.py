# Generated by Django 2.2.1 on 2019-05-31 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Announcements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcements',
            name='pdf',
            field=models.FileField(blank=True, upload_to='announcements/pdfs/'),
        ),
    ]