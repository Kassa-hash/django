from django.contrib import admin
from employe import views
from employe.views import employee_list
from django.urls import path

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
]
