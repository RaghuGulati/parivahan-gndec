# Generated by Django 3.0.3 on 2020-04-25 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0033_auto_20200425_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pgblock',
            name='id',
        ),
        migrations.AddField(
            model_name='pgblock',
            name='employee_id',
            field=models.CharField(default='E001', max_length=4, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]