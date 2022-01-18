# Generated by Django 3.1.3 on 2021-12-30 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubajax', '0029_ubntmodeltest_rrsflag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ubfail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=50)),
                ('failwrite', models.CharField(max_length=200)),
                ('timewrite', models.DateTimeField(auto_now_add=True, verbose_name='Записано')),
            ],
        ),
        migrations.CreateModel(
            name='Ubsuccess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=50)),
                ('successwrite', models.CharField(max_length=200)),
                ('timewrite', models.DateTimeField(auto_now_add=True, verbose_name='Записано')),
            ],
        ),
    ]
