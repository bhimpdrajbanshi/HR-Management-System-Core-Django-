from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    # Show session expired message
    if request.method == "GET" and request.GET.get("next"):
        messages.warning(
            request,
            "Your session has expired. Please log in again."
        )

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(
            email=email,
            password=password
        )

        if user:
            login(request, user)
            return redirect("dashboard/")

        messages.error(request, "Invalid username or password")
    return render(request, "accounts/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")
