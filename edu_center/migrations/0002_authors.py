# Generated by Django 5.0.6 on 2024-06-29 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu_center', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=50)),
                ('autobiorophy', models.TextField()),
                ('birth_date', models.DateTimeField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
