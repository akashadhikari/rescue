# Generated by Django 3.1.1 on 2020-09-10 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Need',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requirement', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('address', models.CharField(max_length=140)),
                ('contact', models.CharField(max_length=15)),
                ('description', models.TextField(max_length=1000)),
                ('needs', models.ManyToManyField(related_name='needs', to='connect.Need')),
            ],
        ),
    ]