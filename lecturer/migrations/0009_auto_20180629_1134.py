# Generated by Django 2.0.4 on 2018-06-29 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lecturer', '0008_auto_20180629_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firsthallvenuearrangement',
            name='lecturer_one',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lecturer_one_first', to='lecturer.LecturerProfile'),
        ),
        migrations.AlterField(
            model_name='firsthallvenuearrangement',
            name='lecturer_three',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lecturer_three_first', to='lecturer.LecturerProfile'),
        ),
        migrations.AlterField(
            model_name='firsthallvenuearrangement',
            name='lecturer_two',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lecturer_two_first', to='lecturer.LecturerProfile'),
        ),
    ]
