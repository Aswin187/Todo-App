# Generated by Django 4.1 on 2022-08-13 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TODOAPP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2001-07-18'),
            preserve_default=False,
        ),
    ]
