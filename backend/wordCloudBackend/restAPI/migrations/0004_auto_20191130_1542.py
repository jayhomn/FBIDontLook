# Generated by Django 2.2.7 on 2019-11-30 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restAPI', '0003_auto_20191130_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='successLogin',
            field=models.BooleanField(default=False),
        ),
    ]
