# Generated by Django 2.0.6 on 2018-06-30 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register_app', '0004_article'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
    ]