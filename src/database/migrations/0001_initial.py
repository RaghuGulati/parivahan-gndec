# Generated by Django 3.0.3 on 2020-03-12 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField()),
                ('urn', models.IntegerField()),
                ('crn', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('aadhar_no', models.IntegerField()),
                ('branch', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('section', models.CharField(max_length=5)),
                ('hosteler_or_dayscollar', models.CharField(max_length=50)),
                ('photo', models.FileField(upload_to='pics')),
                ('class_calculated', models.CharField(max_length=50)),
            ],
        ),
    ]