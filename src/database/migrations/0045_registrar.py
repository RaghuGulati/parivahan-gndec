# Generated by Django 3.0.3 on 2020-05-06 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0044_auto_20200502_0938'),
    ]

    operations = [
        migrations.CreateModel(
            name='registrar',
            fields=[
                ('unique_id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=20)),
            ],
        ),
    ]