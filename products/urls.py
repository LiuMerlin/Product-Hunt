from django.urls import path
from .import views
urlpatterns = [
    path('publish/', views.publish, name='发布页面'),
    path('<int:product_id>', views.detail, name='产品细节'),


]