"""
URL configuration for tienda_online project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from core.views import dashboard   # IMPORTANTE: Vista principal

urlpatterns = [
    path('admin/', admin.site.urls),

    # Página principal del sistema
    path('', dashboard, name='dashboard'),

    # URLs de la app reports (reportes PDF)
    path('reports/', include('reports.urls')),
]
