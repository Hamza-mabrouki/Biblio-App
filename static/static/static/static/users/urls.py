from django.urls import include, path
from .views import signup, facture
from . import views


urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("facture/", views.facture, name="facture"),

]
