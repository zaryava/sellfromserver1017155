# Generated by Django 3.1.3 on 2021-12-29 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ubajax', '0027_auto_20211229_0930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ubntmodeltest',
            name='distributed_system_onoff',
        ),
    ]
