# Generated by Django 4.2.7 on 2023-11-23 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='client_full_name',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='clients',
            name='country',
            field=models.CharField(max_length=140),
        ),
    ]