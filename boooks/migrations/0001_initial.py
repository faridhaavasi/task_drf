# Generated by Django 4.1.7 on 2023-02-27 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('auther', models.CharField(max_length=50)),
                ('serial_number', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
