from django.shortcuts import render
from django.conf import settings

def dashboard(request):
    return render(request, "dashboard.html", {
        "show_reports": settings.ENABLE_REPORTS
    })

