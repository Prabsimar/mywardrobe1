# Generated by Django 3.0.7 on 2020-09-04 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
