# Generated by Django 2.0.3 on 2018-04-03 03:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kpapp', '0009_auto_20180330_0343'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_obj',
            name='resume',
            field=models.FileField(default=2, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student_obj',
            name='roll_no',
            field=models.IntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]