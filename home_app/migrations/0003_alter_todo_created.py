# Generated by Django 5.0.4 on 2024-05-11 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0002_todo_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]