# Generated by Django 3.2.4 on 2021-10-06 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('db', '0002_remove_usermodel_token'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserModel',
        ),
    ]
