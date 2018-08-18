from django.db import models
from django.conf import settings

from student.models import Hall


# Create your models here.
class LecturerProfile(models.Model):
    # lect_title = (('Mr.', 'Mr.'), ('Miss.', 'Miss.'), ('Mrs.', 'Mrs.'))
    # lect_designation = (('Professor', 'Professor'), ('Snr. Lecturer', 'Snr. Lecturer'),('Lecturer I', 'Lecturer I'),
    #                     ('Lecturer II', 'Lecturer II'), ('Assistant Lecturer', 'Assistant Lecturer'),
    #                     ('Graduate Assistant', 'Graduate Assistant'))
    # lect_qualification = (('phd', 'PhD'), ('msc', 'Msc'), ('bsc', 'Bsc'))

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
    title = models.CharField(max_length=6)
    name = models.CharField(max_length=200, default='name')
    designation = models.CharField(max_length=15)
    qualification = models.CharField(max_length=15)
    field_of_specialization = models.CharField(max_length=100)
    course_taught = models.CharField(max_length=200, default='None')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class FirstHallVenueArrangement(models.Model):
    course_code = ((' ', ' '), ('GES 100.1', 'GES 100.1'), ('GES 102.1', 'GES 102.1'), ('CHM 130.1', 'CHM 130.1'),
                   ('MTH 110.1', 'MTH 110.1'), ('MTH 120.1', 'MTH 120.1'), ('PYH 101.1', 'PYH 101.1'),
                   ('PHY 102.1', 'PHY 102.1'))

    lecturer_one = models.ForeignKey(LecturerProfile, on_delete=models.CASCADE, related_name='lecturer_one_first',
                                     blank=True, null=True)
    venue = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='hall_venue_first')
    course = models.CharField(max_length=200, choices=course_code)

    def __str__(self):
        return self.course


class SecondHallVenueArrangement(models.Model):
    course_code = ((' ', ' '), ('GES 100.1', 'GES 100.1'), ('GES 102.1', 'GES 102.1'), ('CHM 130.1', 'CHM 130.1'),
                   ('MTH 110.1', 'MTH 110.1'), ('MTH 120.1', 'MTH 120.1'), ('PYH 101.1', 'PYH 101.1'),
                   ('PHY 102.1', 'PHY 102.1'))

    lecturer_one = models.ForeignKey(LecturerProfile, on_delete=models.CASCADE, related_name='lecturer_one_second',
                                     blank=True, null=True)
    venue = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='hall_venue_second')
    course = models.CharField(max_length=200, choices=course_code)

    def __str__(self):
        return self.course


class lecturerDays(models.Model):
    # lecturer =
    # course =
    # venue =
    # days =
    # time =

    pass