from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name="dashboard"),

    path('cameras/', views.cameras, name="cameras"),
    path('faces/', views.faces, name="faces"),
    path('vehicles/', views.vehicles, name="vehicles"),
    path('alerts/', views.alerts, name="alerts"),
    path('reports/', views.reports, name="reports"),
]
