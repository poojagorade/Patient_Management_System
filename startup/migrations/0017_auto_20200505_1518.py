# Generated by Django 3.0.5 on 2020-05-05 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0016_auto_20200505_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_patients',
            name='date',
            field=models.CharField(max_length=200),
        ),
    ]
