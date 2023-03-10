# Generated by Django 4.1.6 on 2023-03-02 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hike', '0013_alter_hike_name_small_alter_mountain_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrailLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=255)),
                ('hike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hike.hike')),
            ],
        ),
    ]
