from tenant import views
from django.urls import path

urlpatterns = [
    path('', views.view_all_tenants, name='view_all_tenants'),
]