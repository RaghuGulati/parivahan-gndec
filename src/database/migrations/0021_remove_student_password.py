# Generated by Django 3.0.3 on 2020-04-24 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0020_student_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
    ]
