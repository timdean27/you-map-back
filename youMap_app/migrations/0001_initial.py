# Generated by Django 4.1.5 on 2023-01-20 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=500)),
                ('photo_url', models.TextField()),
                ('spot_time', models.DateField()),
            ],
        ),
    ]
