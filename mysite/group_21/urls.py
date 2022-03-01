from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('welcome/', views.welcome, name='welcome'),
    path('email_sign_in/', views.email_sign_in, name='email_sign_in'),
    path('home/', views.home, name='home'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('username_sign_in/', views.username_sign_in, name='username_sign_in'),
    path('registration/', views.registration, name='registration'),
    path('about/', views.about, name='about'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('settings/', views.settings, name='settings'),
]