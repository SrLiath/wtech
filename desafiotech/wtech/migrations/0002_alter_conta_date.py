# Generated by Django 4.1.3 on 2022-11-16 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wtech', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conta',
            name='date',
            field=models.DateField(),
        ),
    ]
