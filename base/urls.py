from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_profile/', views.add_profile, name='add_profile'),
]