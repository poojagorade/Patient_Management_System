# Generated by Django 3.0.5 on 2020-05-05 14:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0017_auto_20200505_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_patients',
            name='given_fee',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='all_patients',
            name='remaining_fee',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='all_patients',
            name='total_fee',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='all_patients',
            name='date',
            field=models.DateField(),
        ),
    ]
