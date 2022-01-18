# Generated by Django 3.0.5 on 2020-07-05 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubajax', '0013_auto_20200705_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataubntall',
            name='udnagrl',
            field=models.FloatField(verbose_name='Трафик приема локального РРС'),
        ),
        migrations.AlterField(
            model_name='dataubntall',
            name='udnagrr',
            field=models.FloatField(verbose_name='Трафик приема удалённого РРС'),
        ),
        migrations.AlterField(
            model_name='dataubntall',
            name='udprml0',
            field=models.IntegerField(verbose_name='Уровень приёма(0) лакального РРС'),
        ),
        migrations.AlterField(
            model_name='dataubntall',
            name='udprml1',
            field=models.IntegerField(verbose_name='Уровень приёма(1) лакального РРС'),
        ),
        migrations.AlterField(
            model_name='dataubntall',
            name='udprmr0',
            field=models.IntegerField(verbose_name='Уровень приёма(0) удалённого РРС'),
        ),
        migrations.AlterField(
            model_name='dataubntall',
            name='udprmr1',
            field=models.IntegerField(verbose_name='Уровень приёма(1) удалённого РРС'),
        ),
        migrations.AlterField(
            model_name='dataubntall',
            name='udspeedl',
            field=models.FloatField(verbose_name='Емкость приёма локального РРС'),
        ),
        migrations.AlterField(
            model_name='dataubntall',
            name='udspeedr',
            field=models.FloatField(verbose_name='Емкость приёма удалённого РРС'),
        ),
    ]
