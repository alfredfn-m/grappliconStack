# Generated by Django 4.0.6 on 2022-07-19 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_tournament_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Champions',
            new_name='Champion',
        ),
    ]
