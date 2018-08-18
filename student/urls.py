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

from django.urls import path

from . import views

app_name='portal'
urlpatterns = [
    path('', views.time_table_first, name='time_table_first'),
    path('second-semester/', views.time_table_second, name='time_table_second'),
    # path('year-one-time-table/', views.time_table, name='time_table'),
    path('courses/year-one/first-semester', views.courses_first, name='courses_first'),
    path('courses/year-one/second-semester', views.courses_second, name='courses_second'),
]
