# Generated by Django 2.2.12 on 2020-06-21 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0013_auto_20200621_1844'),
    ]

    operations = [
        migrations.RenameField(
            model_name='replytoreply',
            old_name='this_reply',
            new_name='reply_reply',
        ),
        migrations.RenameField(
            model_name='replytoreply',
            old_name='this_respondent',
            new_name='reply_respondent',
        ),
    ]
