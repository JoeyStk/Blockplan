# Generated by Django 4.1 on 2022-09-03 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0013_alter_class_options_alter_plan_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='week',
            name='end_date',
            field=models.DateField(blank=True, verbose_name='Enddatum'),
        ),
        migrations.AlterField(
            model_name='week',
            name='start_date',
            field=models.DateField(blank=True, verbose_name='Startdatum'),
        ),
    ]
