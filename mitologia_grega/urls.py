# Arquivo: blog_mitologia/mitologia_grega/urls.py

from django.contrib import admin
from django.urls import path
from . import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('deuses/<str:nome_deus>/', views.detalhes_deus, name='detalhes_deus'),
]