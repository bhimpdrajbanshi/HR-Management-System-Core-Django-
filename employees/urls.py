from django.urls import path
from . import views

urlpatterns = [

    path("create/", views.employees_create, name="employees_create" ),
    path("list/", views.employees_list, name="employees_list" ),
    path("delete/<int:employee_id>/", views.employee_delete,name="employee_delete"),
]