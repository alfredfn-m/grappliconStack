# Generated by Django 4.0.6 on 2022-07-24 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_result_competitora_alter_result_competitorb_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='competitorA',
        ),
        migrations.AddField(
            model_name='result',
            name='competitorA',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='competitorA', to='accounts.competitor'),
        ),
        migrations.RemoveField(
            model_name='result',
            name='competitorB',
        ),
        migrations.AddField(
            model_name='result',
            name='competitorB',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CompetitorB', to='accounts.competitor'),
        ),
        migrations.RemoveField(
            model_name='result',
            name='winner',
        ),
        migrations.AddField(
            model_name='result',
            name='winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Winner', to='accounts.competitor'),
        ),
    ]
