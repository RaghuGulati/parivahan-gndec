# Generated by Django 3.0.3 on 2020-05-02 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0043_advisor_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.FileField(upload_to='./student_photo/'),
        ),
    ]