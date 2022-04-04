from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='election-home'),
    path('dpt_validation/', views.validation, name='election-validation'),
    path('statistic/', views.statistic, name='election-statistic')
]