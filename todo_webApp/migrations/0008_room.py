# Generated by Django 4.1.1 on 2022-10-24 12:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_webApp', '0007_chartaapp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=1000000)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 24, 12, 17, 5, 924024, tzinfo=datetime.timezone.utc))),
                ('room', models.CharField(max_length=2000000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_webApp.chartaapp')),
            ],
        ),
    ]
