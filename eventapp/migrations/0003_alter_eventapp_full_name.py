# Generated by Django 4.2.5 on 2023-09-13 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0002_eventapp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventapp',
            name='full_name',
            field=models.CharField(max_length=120),
        ),
    ]
