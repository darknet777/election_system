from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='election-home'),
    path('validation/', views.validation, name='election-validation'),
    path('voting/', views.voting, name='election-voting'),
    path('voting/vote/<int:id>', views.voterecord, name='election-vote'),
    path('statistic/', views.statistic, name='election-statistic'),
    path('about/', views.about, name='election-about'),
]