# Generated by Django 3.1.3 on 2020-12-05 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_userotp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userotp',
            name='user',
        ),
        migrations.AlterField(
            model_name='userotp',
            name='otp',
            field=models.IntegerField(),
        ),
    ]
