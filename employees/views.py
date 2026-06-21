from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db import transaction

from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

from setup.models import Role
from employees.models import Employee
from accounts.models import User

from employees.validation.validation_employee import validate_employee_create

# Create your views here.

@login_required
def employees_create(request):
   
   if request.method == "POST":
      print(request.POST)
      roles = Role.objects.filter(status="active")
        
      employee_account_data, employee_profile_data, json_error = validate_employee_create(request.POST)
        
      if json_error:
         return render(request, "employees_create.html", {
               "errors": json_error,
               "roles": roles
         })
      # Create User
      user = User.objects.create_user(
            email=employee_account_data["email"],
            username=employee_account_data["username"],
            password=employee_account_data["username"],   
            role_id=employee_account_data["role_id"],
      )
      # Create Employee
      with transaction.atomic():
         Employee.objects.create(
               user_id = user.id,
               first_name=employee_profile_data["first_name"],
               middle_name=employee_profile_data["middle_name"],
               last_name=employee_profile_data["last_name"],
               created_by=request.user,
         )
         
      return redirect("employees_list")

   roles = Role.objects.filter(status="active")
   return render(request, "employees_create.html", {"roles": roles})

@login_required
def employees_list(request):
   employees = Employee.objects.filter(is_void=True)
   roles = Role.objects.filter(status="active")
   return render(request, "employee_list.html", {"employees": employees,"roles": roles})


def employee_delete(request, employee_id):

    try:

        with transaction.atomic():

            employee = get_object_or_404(
                Employee,
                id=employee_id,
                is_void=False
            )

            employee.is_void = True
            employee.save(
                update_fields=["is_void"]
            )

        messages.success(
            request,
            "Employee deleted successfully."
        )

    except Exception as e:

        messages.error(
            request,
            f"Failed to delete employee. {str(e)}"
        )

    return redirect("employees_list")