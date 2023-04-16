from django.shortcuts import render
from django.http import HttpRequest
from .forms import SignUpForm


def signup(request):
    form = SignUpForm
    # return render(request, "registration\signup.html", {'form': form})
    return render(request, "registration\signup.html", {'form': form})


def facture(request):
    return render(request, "users/facture.html")
