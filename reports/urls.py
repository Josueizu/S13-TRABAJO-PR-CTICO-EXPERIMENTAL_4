from django.urls import path
from . import views

urlpatterns = [
    path('export/', views.export_pdf, name='export_pdf')
]

