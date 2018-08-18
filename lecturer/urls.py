"""studentportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import login, logout

from . import views as account_view

app_name='accounts'
urlpatterns = [
    path('register/', account_view.user_registration, name='register'),
    path('login/', login, {'template_name': 'accounts/login.html'}, name='login'),
    path('logout/', logout, {'next_page': '/lecturer/login/'}, name='logout'),
    path('department-lecturers/', account_view.lecturer_list, name='lecturer_list'),
    # path('department-lecturers/<int:id>/', account_view.lecturer_detail, name='lecturer_details'),
    # path('profile/lecture-days/', account_view.lecture_days, name='edit'),

]
