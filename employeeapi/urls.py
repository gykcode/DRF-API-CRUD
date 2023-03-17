from django.urls import re_path
from employeeapi import views

urlpatterns = [
    re_path(r'^department$', views.departmentAPI),
    re_path(r'^department/([0-9]+)$', views.departmentAPI),

    re_path(r'^employee$', views.employeeAPI),
    re_path(r'^employee/([0-9]+)$', views.employeeAPI),
]