# Generated by Django 3.1.3 on 2021-07-02 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubajax', '0025_autorestart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autorestart',
            name='schetchik',
            field=models.IntegerField(),
        ),
    ]
