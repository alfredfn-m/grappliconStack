from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('register_user/', views.register_user, name='register_user'),
    path('about/', views.about, name='about'),
    path('tournament/', views.tournament, name='tournament'),
    path('competitor/', views.competitor, name='competitor'),
    path('history/', views.history, name='history'),
    path('account/', views.account, name='account'),
]
