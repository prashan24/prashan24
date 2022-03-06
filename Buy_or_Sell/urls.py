from django.urls import path
from . import views

urlpatterns = [
    path('', views.buy_or_sell, name='home'),
    path('contact', views.contact, name='Contact')
]
