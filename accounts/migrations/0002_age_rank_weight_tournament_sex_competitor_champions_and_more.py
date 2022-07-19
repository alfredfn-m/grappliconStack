# Generated by Django 4.0.6 on 2022-07-19 00:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(choices=[('UP', 'Upcoming: Less than 18'), ('P', 'Prime: Less than 40'), ('MID', 'Middle: 40 to Less than 55'), ('MSTR', 'Masters: 55 or More')], default='UP', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(choices=[('W', 'White'), ('B', 'Blue'), ('P', 'Purple'), ('Bwn', 'Brown'), ('Blk', 'Black')], default='W', max_length=5)),
                ('Age', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.age')),
            ],
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.CharField(choices=[('125', 'Less than 125'), ('135', '125 to Less than 135'), ('145', '135 to Less than 145'), ('155', '145 to Less than 155'), ('165', '155 to Less than 165'), ('175', '165 to Less than 175'), ('185', '175 to Less than 185'), ('195', '185 to Less than 195'), ('205', '195 to Less than 205'), ('215', '205 to Less than 215'), ('225', '215 to Less than 225'), ('235', '225 to Less than 235'), ('245', '235 to Less than 245'), ('H', '145 or More')], default='125', max_length=4)),
                ('number_of_competitors', models.IntegerField()),
                ('Rank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.rank')),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_tournament', models.DateTimeField(auto_now_add=True)),
                ('address', models.CharField(default='Address', max_length=100)),
                ('city', models.CharField(default='City', max_length=100)),
                ('state_or_province', models.CharField(default='State or Province', max_length=100)),
                ('nation', models.CharField(default='Nation', max_length=100)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=2)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.tournament')),
            ],
        ),
        migrations.CreateModel(
            name='Competitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('weight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.weight')),
            ],
        ),
        migrations.CreateModel(
            name='Champions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=2)),
                ('age', models.CharField(choices=[('UP', 'Upcoming: Less than 18'), ('P', 'Prime: Less than 40'), ('MID', 'Middle: 40 to Less than 55'), ('MSTR', 'Masters: 55 or More')], default='UP', max_length=5)),
                ('rank', models.CharField(choices=[('W', 'White'), ('B', 'Blue'), ('P', 'Purple'), ('Bwn', 'Brown'), ('Blk', 'Black')], default='W', max_length=5)),
                ('weight', models.CharField(choices=[('125', 'Less than 125'), ('135', '125 to Less than 135'), ('145', '135 to Less than 145'), ('155', '145 to Less than 155'), ('165', '155 to Less than 165'), ('175', '165 to Less than 175'), ('185', '175 to Less than 185'), ('195', '185 to Less than 195'), ('205', '195 to Less than 205'), ('215', '205 to Less than 215'), ('225', '215 to Less than 225'), ('235', '225 to Less than 235'), ('245', '235 to Less than 245'), ('H', '145 or More')], default='125', max_length=4)),
                ('champion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.tournament')),
            ],
        ),
        migrations.AddField(
            model_name='age',
            name='sex',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.sex'),
        ),
    ]