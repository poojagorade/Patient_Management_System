# Generated by Django 3.0.5 on 2020-05-06 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0025_remove_all_patients_some'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_patients',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
