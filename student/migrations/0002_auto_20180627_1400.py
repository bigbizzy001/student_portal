# Generated by Django 2.0.4 on 2018-06-27 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HallVenueArrangement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='hall',
            name='hall',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=10),
        ),
        migrations.AlterField(
            model_name='timetableone',
            name='eighth_course',
            field=models.CharField(blank=True, choices=[(' ', ' '), ('GES 100.1', 'GES 100.1'), ('GES 102.1', 'GES 102.1'), ('CHM 130.1', 'CHM 130.1'), ('MTH 110.1', 'MTH 110.1'), ('MTH 120.1', 'MTH 120.1'), ('PYH 101.1', 'PYH 101.1'), ('PHY 102.1', 'PHY 102.1')], max_length=10),
        ),
        migrations.AlterField(
            model_name='timetableone',
            name='fifth_course',
            field=models.CharField(blank=True, choices=[(' ', ' '), ('GES 100.1', 'GES 100.1'), ('GES 102.1', 'GES 102.1'), ('CHM 130.1', 'CHM 130.1'), ('MTH 110.1', 'MTH 110.1'), ('MTH 120.1', 'MTH 120.1'), ('PYH 101.1', 'PYH 101.1'), ('PHY 102.1', 'PHY 102.1')], max_length=10),
        ),
        migrations.AlterField(
            model_name='timetableone',
            name='first_course',
            field=models.CharField(blank=True, choices=[(' ', ' '), ('GES 100.1', 'GES 100.1'), ('GES 102.1', 'GES 102.1'), ('CHM 130.1', 'CHM 130.1'), ('MTH 110.1', 'MTH 110.1'), ('MTH 120.1', 'MTH 120.1'), ('PYH 101.1', 'PYH 101.1'), ('PHY 102.1', 'PHY 102.1')], max_length=10),
        ),
        migrations.AlterField(
            model_name='timetableone',
            name='fourth_course',
            field=models.CharField(blank=True, choices=[(' ', ' '), ('GES 100.1', 'GES 100.1'), ('GES 102.1', 'GES 102.1'), ('CHM 130.1', 'CHM 130.1'), ('MTH 110.1', 'MTH 110.1'), ('MTH 120.1', 'MTH 120.1'), ('PYH 101.1', 'PYH 101.1'), ('PHY 102.1', 'PHY 102.1')], max_length=10),
        ),
        migrations.AlterField(
            model_name='timetableone',
            name='second_course',
            field=models.CharField(blank=True, choices=[(' ', ' '), ('GES 100.1', 'GES 100.1'), ('GES 102.1', 'GES 102.1'), ('CHM 130.1', 'CHM 130.1'), ('MTH 110.1', 'MTH 110.1'), ('MTH 120.1', 'MTH 120.1'), ('PYH 101.1', 'PYH 101.1'), ('PHY 102.1', 'PHY 102.1')], max_length=10),
        ),
        migrations.AlterField(
            model_name='timetableone',
            name='seventh_course',
            field=models.CharField(blank=True, choices=[(' ', ' '), ('GES 100.1', 'GES 100.1'), ('GES 102.1', 'GES 102.1'), ('CHM 130.1', 'CHM 130.1'), ('MTH 110.1', 'MTH 110.1'), ('MTH 120.1', 'MTH 120.1'), ('PYH 101.1', 'PYH 101.1'), ('PHY 102.1', 'PHY 102.1')], max_length=10),
        ),
        migrations.AlterField(
            model_name='timetableone',
            name='sixth_course',
            field=models.CharField(blank=True, choices=[(' ', ' '), ('GES 100.1', 'GES 100.1'), ('GES 102.1', 'GES 102.1'), ('CHM 130.1', 'CHM 130.1'), ('MTH 110.1', 'MTH 110.1'), ('MTH 120.1', 'MTH 120.1'), ('PYH 101.1', 'PYH 101.1'), ('PHY 102.1', 'PHY 102.1')], max_length=10),
        ),
        migrations.AlterField(
            model_name='timetableone',
            name='third_course',
            field=models.CharField(blank=True, choices=[(' ', ' '), ('GES 100.1', 'GES 100.1'), ('GES 102.1', 'GES 102.1'), ('CHM 130.1', 'CHM 130.1'), ('MTH 110.1', 'MTH 110.1'), ('MTH 120.1', 'MTH 120.1'), ('PYH 101.1', 'PYH 101.1'), ('PHY 102.1', 'PHY 102.1')], max_length=10),
        ),
        migrations.AlterField(
            model_name='timetabletwo',
            name='eighth_course',
            field=models.CharField(blank=True, choices=[(' ', ' '), ('GES 101.2', 'GES 101.2'), ('CHM 131.2', 'CHM 131.2'), ('PHY 112.2', 'PHY 112.2'), ('MTH 124.2', 'MTH 124.2'), ('GES 103.2', 'GES 103.2'), ('PYH 103.2', 'PYH 103.2'), ('GLY 101.2', 'GLY 101.2'), ('GLY 102.2', 'GLY 102.2')], max_length=10),
        ),
        migrations.AlterField(
            model_name='timetabletwo',
            name='fifth_course',
            field=models.CharField(blank=True, choices=[(' ', ' '), ('GES 101.2', 'GES 101.2'), ('CHM 131.2', 'CHM 131.2'), ('PHY 112.2', 'PHY 112.2'), ('MTH 124.2', 'MTH 124.2'), ('GES 103.2', 'GES 103.2'), ('PYH 103.2', 'PYH 103.2'), ('GLY 101.2', 'GLY 101.2'), ('GLY 102.2', 'GLY 102.2')], max_length=10),
        ),
        migrations.AlterField(
            model_name='timetabletwo',
            name='first_course',
            field=models.CharField(blank=True, choices=[(' ', ' '), ('GES 101.2', 'GES 101.2'), ('CHM 131.2', 'CHM 131.2'), ('PHY 112.2', 'PHY 112.2'), ('MTH 124.2', 'MTH 124.2'), ('GES 103.2', 'GES 103.2'), ('PYH 103.2', 'PYH 103.2'), ('GLY 101.2', 'GLY 101.2'), ('GLY 102.2', 'GLY 102.2')], max_length=10),
        ),
        migrations.AlterField(
            model_name='timetabletwo',
            name='fourth_course',
            field=models.CharField(blank=True, choices=[(' ', ' '), ('GES 101.2', 'GES 101.2'), ('CHM 131.2', 'CHM 131.2'), ('PHY 112.2', 'PHY 112.2'), ('MTH 124.2', 'MTH 124.2'), ('GES 103.2', 'GES 103.2'), ('PYH 103.2', 'PYH 103.2'), ('GLY 101.2', 'GLY 101.2'), ('GLY 102.2', 'GLY 102.2')], max_length=10),
        ),
        migrations.AlterField(
            model_name='timetabletwo',
            name='second_course',
            field=models.CharField(blank=True, choices=[(' ', ' '), ('GES 101.2', 'GES 101.2'), ('CHM 131.2', 'CHM 131.2'), ('PHY 112.2', 'PHY 112.2'), ('MTH 124.2', 'MTH 124.2'), ('GES 103.2', 'GES 103.2'), ('PYH 103.2', 'PYH 103.2'), ('GLY 101.2', 'GLY 101.2'), ('GLY 102.2', 'GLY 102.2')], max_length=10),
        ),
        migrations.AlterField(
            model_name='timetabletwo',
            name='seventh_course',
            field=models.CharField(blank=True, choices=[(' ', ' '), ('GES 101.2', 'GES 101.2'), ('CHM 131.2', 'CHM 131.2'), ('PHY 112.2', 'PHY 112.2'), ('MTH 124.2', 'MTH 124.2'), ('GES 103.2', 'GES 103.2'), ('PYH 103.2', 'PYH 103.2'), ('GLY 101.2', 'GLY 101.2'), ('GLY 102.2', 'GLY 102.2')], max_length=10),
        ),
        migrations.AlterField(
            model_name='timetabletwo',
            name='sixth_course',
            field=models.CharField(blank=True, choices=[(' ', ' '), ('GES 101.2', 'GES 101.2'), ('CHM 131.2', 'CHM 131.2'), ('PHY 112.2', 'PHY 112.2'), ('MTH 124.2', 'MTH 124.2'), ('GES 103.2', 'GES 103.2'), ('PYH 103.2', 'PYH 103.2'), ('GLY 101.2', 'GLY 101.2'), ('GLY 102.2', 'GLY 102.2')], max_length=10),
        ),
        migrations.AlterField(
            model_name='timetabletwo',
            name='third_course',
            field=models.CharField(blank=True, choices=[(' ', ' '), ('GES 101.2', 'GES 101.2'), ('CHM 131.2', 'CHM 131.2'), ('PHY 112.2', 'PHY 112.2'), ('MTH 124.2', 'MTH 124.2'), ('GES 103.2', 'GES 103.2'), ('PYH 103.2', 'PYH 103.2'), ('GLY 101.2', 'GLY 101.2'), ('GLY 102.2', 'GLY 102.2')], max_length=10),
        ),
    ]
