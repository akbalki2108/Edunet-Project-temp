from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('load_data/', views.load_data, name='load_data'),
    path('filter_data/', views.filter_data, name='filter_data'),
    path('about/', views.about, name='about'),
]
