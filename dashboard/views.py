from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard_home(request):
    return render(request, "dashboard/index.html")


@login_required
def cameras(request):
    return render(request, "dashboard/cameras.html")


@login_required
def faces(request):
    return render(request, "dashboard/faces.html")


@login_required
def vehicles(request):
    return render(request, "dashboard/vehicles.html")


@login_required
def alerts(request):
    return render(request, "dashboard/alerts.html")


@login_required
def reports(request):
    return render(request, "dashboard/reports.html")
