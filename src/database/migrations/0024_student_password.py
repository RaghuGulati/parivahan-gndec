# Generated by Django 3.0.3 on 2020-04-24 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0023_remove_student_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.IntegerField(default=123456),
            preserve_default=False,
        ),
    ]