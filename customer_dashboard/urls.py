from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.customer_dashboard, name='customer_dashboard'),
]
