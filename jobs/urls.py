from django.urls import path,include
from . import views
from django.shortcuts import redirect
from django.urls import reverse

urlpatterns = [
    path('', views.jobs, name='jobs'),
    ]
