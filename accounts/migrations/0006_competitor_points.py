# Generated by Django 4.0.6 on 2022-07-19 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_champions_champion'),
    ]

    operations = [
        migrations.AddField(
            model_name='competitor',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]