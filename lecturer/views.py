from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import LecturerRegistrationForm, LecturerProfileEditForm, UserEditForm
from .models import LecturerProfile


# Create your views here.
def user_registration(request):
    if request.method == 'POST':
        form = LecturerRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            profile = LecturerProfile.objects.create(user=new_user)
            return redirect('accounts:login', {'new_user': new_user})
    else:
        form = LecturerRegistrationForm()

    template = 'accounts/registration.html'
    context = {'form': form}
    return render(request, template, context)


@login_required
def lecture_venues_arrangements(request):

    template = 'accounts/view_lecture_days.html'
    context = {}
    return render(request, template, context)


def lecturer_list(request):
    list = LecturerProfile.objects.all()

    template = 'accounts/lecturer_list.html'
    context = {'lists': list}
    return render(request, template, context)


# def logout_user(request):
#     return render(request, 'accounts/view_profile.html')