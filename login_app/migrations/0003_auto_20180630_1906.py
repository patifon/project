# Generated by Django 2.0.6 on 2018-06-30 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_auto_20180630_1903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authusers',
            old_name='password',
            new_name='user_password',
        ),
    ]