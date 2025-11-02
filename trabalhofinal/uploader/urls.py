from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload'),
    path('analise/', views.analysis_view, name='analysis'),
    path('predicao/', views.prediction_view, name='prediction'),
]