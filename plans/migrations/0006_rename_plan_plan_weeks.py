# Generated by Django 4.1 on 2022-08-19 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0005_week_week_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plan',
            old_name='plan',
            new_name='weeks',
        ),
    ]
