# Generated by Django 4.1.6 on 2023-03-02 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hike', '0014_traillinks'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TrailLinks',
            new_name='TrailLink',
        ),
    ]