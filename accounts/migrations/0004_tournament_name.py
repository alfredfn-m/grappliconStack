# Generated by Django 4.0.6 on 2022-07-19 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_tournament_date_of_tournament'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='name',
            field=models.CharField(default='Tournament Name', max_length=100),
        ),
    ]
