# Generated by Django 2.2.12 on 2020-06-21 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0011_replytoreply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
