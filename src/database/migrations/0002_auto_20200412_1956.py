# Generated by Django 3.0.3 on 2020-04-12 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='FM_Name',
            new_name='parents_name',
        ),
    ]
