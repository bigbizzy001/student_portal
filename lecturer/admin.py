from django.contrib import admin

from .models import LecturerProfile, FirstHallVenueArrangement, SecondHallVenueArrangement


# Register your models here.
class LecturerProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'name', 'designation', 'qualification', 'field_of_specialization', 'course_taught']

admin.site.register(LecturerProfile, LecturerProfileAdmin)


class FirstHallVenueArrangementAdmin(admin.ModelAdmin):
    list_display = ['course', 'venue', 'lecturer_one']

admin.site.register(FirstHallVenueArrangement, FirstHallVenueArrangementAdmin)


class SecondHallVenueArrangementAdmin(admin.ModelAdmin):
    list_display = ['course', 'venue', 'lecturer_one']

admin.site.register(SecondHallVenueArrangement, SecondHallVenueArrangementAdmin)

