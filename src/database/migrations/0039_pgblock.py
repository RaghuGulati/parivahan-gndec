# Generated by Django 3.0.3 on 2020-04-25 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0038_delete_pgblock'),
    ]

    operations = [
        migrations.CreateModel(
            name='PgBlock',
            fields=[
                ('employee_id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('employee_name', models.CharField(max_length=50)),
                ('head_name', models.CharField(max_length=50)),
            ],
        ),
    ]