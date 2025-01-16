from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.salorformpage, name='solarform'),
    path('export-excel/', views.export_excel, name='export_excel'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)