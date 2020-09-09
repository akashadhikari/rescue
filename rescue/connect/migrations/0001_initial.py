# Generated by Django 3.1.1 on 2020-09-09 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HelpCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('address', models.CharField(max_length=140)),
                ('contact', models.CharField(max_length=15)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
    ]
