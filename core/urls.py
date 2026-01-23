from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view, index, about, profile_view

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path("register/", register_view, name="register"),
    path("login/", auth_views.LoginView.as_view(
        template_name="auth/login.html"
    ), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("profile/", profile_view, name="profile"),
]