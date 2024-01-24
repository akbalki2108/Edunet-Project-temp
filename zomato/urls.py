from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('load_data/', views.load_data, name='load_data'),
    path('filter_data/', views.filter_data, name='filter_data'),
    path('contact/', views.contact, name='contact'),
    path('', views.index, name='index'),
    path('heatmap_map/', TemplateView.as_view(template_name="heatmap_map.html"), name='heatmap_map'),
]
