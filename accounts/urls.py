from django.urls import path
from . import views

urlpatterns = [

    path("", views.login_view, name="login" ),
    # path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout" ),

    path("profile/", views.profile_view, name="profile"),

    # path("forgot-password/", views.forgot_password, name="forgot_password"),
    # path("reset-password/", views.reset_password, name="reset_password"),
    # path("change-password/", views.change_password, name="change_password"),
]