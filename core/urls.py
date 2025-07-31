from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apply/', views.apply_job, name='apply_job'),
]
