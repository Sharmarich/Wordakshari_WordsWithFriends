# Generated by Django 4.0.3 on 2022-04-09 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordgame', '0008_alter_room_word'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='name',
        ),
        migrations.AlterField(
            model_name='room',
            name='word',
            field=models.CharField(default='AAPLE', max_length=20),
        ),
    ]
