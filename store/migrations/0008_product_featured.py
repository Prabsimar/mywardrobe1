# Generated by Django 3.0.7 on 2020-09-06 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20200905_0406'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
