from django.shortcuts import render


# Create your views here.
def create_account(request):
    return render(request, 'create_account.html')


def login(request):
    return render(request, "login.html")


def create_profile(request):
    return render(request, "create_profile.html")


def change_password(request):
    return render(request, "change_password.html")


def view_label(request):
    return render(request, "view_label.html")
