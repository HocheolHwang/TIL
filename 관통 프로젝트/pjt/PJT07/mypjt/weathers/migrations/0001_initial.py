# Generated by Django 4.2.6 on 2023-10-27 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField()),
                ('feels_like', models.FloatField()),
                ('de_txt', models.DateTimeField()),
            ],
        ),
    ]
