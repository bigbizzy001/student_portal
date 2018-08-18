from django.shortcuts import render
from .models import FirstSemester, SecondSemester, TimeTableOne, TimeTableTwo

from lecturer.models import FirstHallVenueArrangement, SecondHallVenueArrangement


# Create your views here.
# def home(request):
#     return render(request, 'portal/home.html')


# def time_table(request):
#     return render(request, 'portal/year_one.html')


def courses_first(request):
    total_cu = 18
    first_semester = FirstSemester.objects.all()
    # halls = Hall.objects.all()

    template = 'portal/courses_first.html'
    context = {'first_semester': first_semester, 'cu': total_cu}
    return render(request, template, context)


def courses_second(request):
    totalcu = 18
    second_semester = SecondSemester.objects.all()
    # cu = SecondSemester.objects.filter('credit_unit')
    # print(cu)
    template = 'portal/courses_second.html'
    context = {'second_semester': second_semester, 'cu': totalcu}
    return render(request, template, context)


def time_table_first(request):
    first_semester = TimeTableOne.objects.all()
    first_arrangements = FirstHallVenueArrangement.objects.all()

    template = 'portal/home.html'
    context = {'first_time_table': first_semester, 'first_arrangements':first_arrangements}
    return render(request, template, context)


def time_table_second(request):
    second_semester = TimeTableTwo.objects.all()
    second_arrangements = SecondHallVenueArrangement.objects.all()

    template = 'portal/second.html'
    context = {'second_time_table': second_semester, 'second_arrangements':second_arrangements}
    return render(request, template, context)

