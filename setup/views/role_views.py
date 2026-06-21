from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from setup.models import Role

from setup.validation.role.role_validation import validate_role_create


@login_required
def department_list(request):
   return render(request, "department/department_list.html")


@login_required
def role_list(request):
   roles = Role.objects.filter(status="active")
   return render(request, "role/role_list.html", {"roles": roles})

@login_required
def role(request):
    return render(request, "role/role_create.html")

@login_required
def role_create(request):
    if request.method == "POST":
        
        role_name, status, json_error = validate_role_create(request.POST)
        
        if json_error:
            return render(request, "role/role_create.html", {
                "errors": json_error
            })
        Role.objects.create(
            role_name=role_name,
            status=status
        )
        return redirect("role_list")

    return render(request, "role/role_create.html")