from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'group_21/welcome.html')


def welcome(request):
    return render(request, 'group_21/welcome.html')


def email_sign_in(request):
    return render(request, 'group_21/email_sign_in.html')

def home(request):
    return render(request, 'group_21/home.html')

def reset_password(request):
    return render(request, 'group_21/reset_password.html')


def username_sign_in(request):
    return render(request, 'group_21/username_sign_in.html')


def registration(request):
    return render(request, 'group_21/registration.html')

def about(request):
    return render(request, 'group_21/about.html')

def leaderboard(request):
    return render(request, 'group_21/leaderboard.html')

def settings(request):
    return render(request, 'group_21/settings.html')