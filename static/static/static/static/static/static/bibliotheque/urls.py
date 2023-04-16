from django.urls import path
from .views import list_books, add, get_one_book, contact
from . import views

urlpatterns = [
    # path("contact/", contact),
    # path("", list_books),
    # path("<str:id>", get_one_book),
    path("search/", views.html, name="search_space"),
    path("blog/", views.html3, name="blog_space"),
    # path("add/",add),
    # path("accuiel/", accueil),

]
