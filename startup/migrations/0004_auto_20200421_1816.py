# Generated by Django 3.0.5 on 2020-04-21 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0003_auto_20200421_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_patients',
            name='fname',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
