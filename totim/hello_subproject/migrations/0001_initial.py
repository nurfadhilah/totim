# Generated by Django 5.0.6 on 2024-05-16 01:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('menid', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('menname', models.TextField(max_length=225)),
                ('menroomno', models.CharField(default='sk2', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Shobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('hobby', models.TextField()),
                ('gender', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('stuid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('stuname', models.CharField(max_length=255)),
                ('stuemail', models.CharField(max_length=255)),
                ('stuage', models.PositiveSmallIntegerField(default=0)),
                ('stumentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello_subproject.mentor')),
            ],
        ),
    ]
