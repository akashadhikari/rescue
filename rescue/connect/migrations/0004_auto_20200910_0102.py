# Generated by Django 3.1.1 on 2020-09-10 01:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0003_auto_20200910_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='helpcenter',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='helpcenter',
            name='needs',
            field=models.ManyToManyField(related_name='help_center_provisions', to='connect.Need'),
        ),
        migrations.AddField(
            model_name='helpcenter',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='help',
            name='needs',
            field=models.ManyToManyField(related_name='help_provisions', to='connect.Need'),
        ),
        migrations.CreateModel(
            name='SomeoneNeedsHelp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('address', models.CharField(max_length=140)),
                ('contact', models.CharField(max_length=15)),
                ('description', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('number_of_people', models.IntegerField()),
                ('needs', models.ManyToManyField(related_name='need_help', to='connect.Need')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
