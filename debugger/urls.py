from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('run/', views.run_code, name='run_code'),
    path('about/', views.about, name='about'),
]
