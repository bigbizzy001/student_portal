# Generated by Django 2.0.4 on 2018-06-28 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecturer', '0006_lecturerprofile_course_taught'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturerprofile',
            name='designation',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='lecturerprofile',
            name='title',
            field=models.CharField(max_length=6),
        ),
    ]