from django.urls import path
from . import views

urlpatterns = [

    path("department/list/", views.department_list, name="department_list" ),
    
    path("role/", views.role, name="role" ),
    path("role/create/", views.role_create, name="role_create" ),
    path("role/list/", views.role_list, name="role_list" ),
]