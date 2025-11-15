from django.http import HttpResponse
from django.conf import settings


def export_pdf(request):
    if not settings.ENABLE_REPORTS:
        return HttpResponse("Reportes desactivados")

    return HttpResponse("Aqui iria el PDF generado...")
