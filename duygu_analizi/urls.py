from django.urls import path
from . import views

app_name = 'duygu_analizi'  # Namespace kullanımı için app_name eklendi

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    path('analiz/', views.analiz, name='analiz'),  # Analiz view'inizi buraya ekleyin
]
