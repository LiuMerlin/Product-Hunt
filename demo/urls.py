from django.urls import path
from .import views

urlpatterns = [
    path('bar/', views.ChartView.as_view(), name='demo'),
    path('index', views.IndexView.as_view(), name='demo'),

]
