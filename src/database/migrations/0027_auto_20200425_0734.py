# Generated by Django 3.0.3 on 2020-04-25 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0026_student_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=8),
        ),
    ]
