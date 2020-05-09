# Generated by Django 3.0.5 on 2020-04-29 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0011_auto_20200424_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='Old_Patients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('total_fee', models.IntegerField()),
                ('given_fee', models.IntegerField()),
                ('remaining_fee', models.IntegerField()),
            ],
        ),
    ]
