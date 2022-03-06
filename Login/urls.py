from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_view, name='Login'),
    path('logout', views.logout, name='Logout'),
    path('dashboard', views.dashboard, name="dashboard"),
]