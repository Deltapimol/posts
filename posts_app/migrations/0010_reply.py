# Generated by Django 2.2.12 on 2020-06-19 18:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts_app', '0009_delete_reply'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.CharField(max_length=300)),
                ('reply_datetime', models.DateTimeField(null=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts_app.Comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts_app.Post')),
                ('respondent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
