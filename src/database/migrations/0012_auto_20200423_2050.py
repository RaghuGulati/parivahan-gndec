# Generated by Django 3.0.3 on 2020-04-23 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0011_auto_20200423_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clerkoffice',
            name='clerk_id',
            field=models.CharField(max_length=6, primary_key=True, serialize=False),
        ),
    ]
