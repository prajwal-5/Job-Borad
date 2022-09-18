# Generated by Django 4.1.1 on 2022-09-16 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=500)),
                ('location', models.CharField(max_length=250)),
                ('deadline', models.DateTimeField()),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
