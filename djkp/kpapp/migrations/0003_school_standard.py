# Generated by Django 2.0.3 on 2018-03-22 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kpapp', '0002_auto_20180315_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=100)),
                ('year_estd', models.DateField(blank=True)),
                ('studentsCount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard', models.IntegerField()),
                ('section_count', models.IntegerField()),
                ('studentsCount', models.IntegerField()),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kpapp.School')),
            ],
        ),
    ]
