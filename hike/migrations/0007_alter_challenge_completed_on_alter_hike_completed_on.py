# Generated by Django 4.1.6 on 2023-02-09 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hike', '0006_alter_challenge_completed_on_alter_hike_range'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='completed_on',
            field=models.DateField(blank=True, null=True, verbose_name='date completed'),
        ),
        migrations.AlterField(
            model_name='hike',
            name='completed_on',
            field=models.DateField(blank=True, null=True, verbose_name='date completed'),
        ),
    ]
