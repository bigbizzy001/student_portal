# Generated by Django 2.0.4 on 2018-06-29 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20180629_1109'),
        ('lecturer', '0007_auto_20180628_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirstHallVenueArrangement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(choices=[(' ', ' '), ('GES 100.1', 'GES 100.1'), ('GES 102.1', 'GES 102.1'), ('CHM 130.1', 'CHM 130.1'), ('MTH 110.1', 'MTH 110.1'), ('MTH 120.1', 'MTH 120.1'), ('PYH 101.1', 'PYH 101.1'), ('PHY 102.1', 'PHY 102.1')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SecondHallVenueArrangement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(choices=[(' ', ' '), ('GES 100.1', 'GES 100.1'), ('GES 102.1', 'GES 102.1'), ('CHM 130.1', 'CHM 130.1'), ('MTH 110.1', 'MTH 110.1'), ('MTH 120.1', 'MTH 120.1'), ('PYH 101.1', 'PYH 101.1'), ('PHY 102.1', 'PHY 102.1')], max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='lecturerprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='secondhallvenuearrangement',
            name='lecturer_one',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='lecturer_one_second', to='lecturer.LecturerProfile'),
        ),
        migrations.AddField(
            model_name='secondhallvenuearrangement',
            name='lecturer_three',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='lecturer_three_second', to='lecturer.LecturerProfile'),
        ),
        migrations.AddField(
            model_name='secondhallvenuearrangement',
            name='lecturer_two',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='lecturer_two_second', to='lecturer.LecturerProfile'),
        ),
        migrations.AddField(
            model_name='secondhallvenuearrangement',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hall_venue_second', to='student.Hall'),
        ),
        migrations.AddField(
            model_name='firsthallvenuearrangement',
            name='lecturer_one',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='lecturer_one_first', to='lecturer.LecturerProfile'),
        ),
        migrations.AddField(
            model_name='firsthallvenuearrangement',
            name='lecturer_three',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='lecturer_three_first', to='lecturer.LecturerProfile'),
        ),
        migrations.AddField(
            model_name='firsthallvenuearrangement',
            name='lecturer_two',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='lecturer_two_first', to='lecturer.LecturerProfile'),
        ),
        migrations.AddField(
            model_name='firsthallvenuearrangement',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hall_venue_first', to='student.Hall'),
        ),
    ]