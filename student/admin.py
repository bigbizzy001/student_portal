from django.contrib import admin
from .models import FirstSemester, SecondSemester, LectureDay, LectureTime, Hall, TimeTableOne, TimeTableTwo


# Register your models here.
class FirstSemesterCourseAdmin(admin.ModelAdmin):
    list_display= ['course_code', 'course_title', 'credit_unit']


admin.site.register(FirstSemester, FirstSemesterCourseAdmin)


class SecondSemesterCourseAdmin(admin.ModelAdmin):
    list_display = ['course_code', 'course_title', 'credit_unit']


admin.site.register(SecondSemester, SecondSemesterCourseAdmin)


class LectureDaysAdmin(admin.ModelAdmin):
    list_display = ['day',]


admin.site.register(LectureDay, LectureDaysAdmin)


class LectureTimeAdmin(admin.ModelAdmin):
    list_display = ['time_from', 'time_to']


admin.site.register(LectureTime, LectureTimeAdmin)


class TimeTableFirstSemesterAdmin(admin.ModelAdmin):
    list_display = ['day', 'first_course', 'second_course', 'third_course', 'fourth_course',
                    'fifth_course', 'sixth_course', 'seventh_course', 'eighth_course']


admin.site.register(TimeTableOne, TimeTableFirstSemesterAdmin)


class TimeTableSecondSemesterAdmin(admin.ModelAdmin):
    list_display = ['day', 'first_course', 'second_course', 'third_course', 'fourth_course',
                    'fifth_course', 'sixth_course', 'seventh_course', 'eighth_course']


admin.site.register(TimeTableTwo, TimeTableSecondSemesterAdmin)


class HallsAdmin(admin.ModelAdmin):
    list_display = ['hall']


admin.site.register(Hall, HallsAdmin)


