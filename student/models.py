from django.db import models


# Create your models here.
class FirstSemester(models.Model):
    course_title = models.CharField(max_length=200)
    course_code = models.CharField(max_length=10)
    credit_unit = models.IntegerField(blank=True)

    def __str__(self):
        return self.course_code


class SecondSemester(models.Model):
    course_title = models.CharField(max_length=200)
    course_code = models.CharField(max_length=10)
    credit_unit = models.IntegerField(blank=True)

    def __str__(self):
        return self.course_code


class LectureDay(models.Model):
    day = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.day


class LectureTime(models.Model):
    time_from = models.TimeField()
    time_to = models.TimeField()


class TimeTableOne(models.Model):
    course_code = ((' ', ' '), ('GES 100.1', 'GES 100.1'), ('GES 102.1', 'GES 102.1'), ('CHM 130.1', 'CHM 130.1'),
                   ('MTH 110.1', 'MTH 110.1'), ('MTH 120.1', 'MTH 120.1'), ('PYH 101.1', 'PYH 101.1'),
                   ('PHY 102.1', 'PHY 102.1'))

    day = models.ForeignKey(LectureDay, on_delete=models.CASCADE, blank=True, related_name='day_first')
    first_course = models.CharField(max_length=10, choices=course_code, blank=True)
    second_course = models.CharField(max_length=10, choices=course_code, blank=True)
    third_course = models.CharField(max_length=10, choices=course_code, blank=True)
    fourth_course = models.CharField(max_length=10, choices=course_code, blank=True)
    fifth_course = models.CharField(max_length=10, choices=course_code, blank=True)
    sixth_course = models.CharField(max_length=10, choices=course_code, blank=True)
    seventh_course = models.CharField(max_length=10, choices=course_code, blank=True)
    eighth_course = models.CharField(max_length=10, choices=course_code, blank=True)

    def __str__(self):
        return 'Year 1 Time Table First'


class TimeTableTwo(models.Model):
    course_code = ((' ', ' '), ('GES 101.2', 'GES 101.2'), ('CHM 131.2', 'CHM 131.2'), ('PHY 112.2', 'PHY 112.2'),
                   ('MTH 124.2', 'MTH 124.2'), ('GES 103.2', 'GES 103.2'), ('PYH 103.2', 'PYH 103.2'),
                   ('GLY 101.2', 'GLY 101.2'), ('GLY 102.2', 'GLY 102.2'))

    day = models.ForeignKey(LectureDay, on_delete=models.CASCADE, blank=True, related_name='day_second')
    first_course = models.CharField(max_length=10, choices=course_code, blank=True)
    second_course = models.CharField(max_length=10, choices=course_code, blank=True)
    third_course = models.CharField(max_length=10, choices=course_code, blank=True)
    fourth_course = models.CharField(max_length=10, choices=course_code, blank=True)
    fifth_course = models.CharField(max_length=10, choices=course_code, blank=True)
    sixth_course = models.CharField(max_length=10, choices=course_code, blank=True)
    seventh_course = models.CharField(max_length=10, choices=course_code, blank=True)
    eighth_course = models.CharField(max_length=10, choices=course_code, blank=True)

    def __str__(self):
        return 'Year 2 Time Table Second'


class Hall(models.Model):
    halls = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'))

    hall = models.CharField(max_length=10,  choices=halls, blank=True)

    def __str__(self):
        return self.hall



