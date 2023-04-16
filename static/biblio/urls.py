
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path
from django.http import HttpResponse


def home(request):
    return HttpResponse("salam")


def accueil(request):
    return render(request, "accueil.html")


urlpatterns = [
    path('bibliotheque_admin/', admin.site.urls),
    path('book/', include("bibliotheque.urls")),
    path('home/', home),
    path('', include("django.contrib.auth.urls")),
    path('', include("users.urls")),
    path('', accueil),
]
