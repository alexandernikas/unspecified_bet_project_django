from django.urls import path, include
from bet_warehouse import views

urlpatterns = [
    path('latest-bets/', views.LatestBetSlips.as_view()),
]