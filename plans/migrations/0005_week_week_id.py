# Generated by Django 4.1 on 2022-08-19 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0004_remove_week_plan_plan_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='week',
            name='week_id',
            field=models.IntegerField(default=1, null=True, verbose_name='Kalendarwoche'),
        ),
    ]