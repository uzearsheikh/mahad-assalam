from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('semester/<int:semester_id>/', views.semester_detail, name='semester_detail'),
    path('marhala/<int:marhala_id>/', views.marhala_detail, name='marhala_detail'),
]
