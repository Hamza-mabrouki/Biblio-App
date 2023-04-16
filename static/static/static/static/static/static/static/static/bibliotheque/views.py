from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookForm, ContactForm
from .models import Book


def list_books(request):

    title = "Welcome"

    get_books = Book.objects.all()

    return render(request, "bibliotheque/index.html", {
        "title": title, "books": get_books,
    })


def get_one_book(request, id):
    book = Book.objects.get(pk=id)
    return render(request, "bibliotheque/show.html", {"book": book})


def add(request):
    form = BookForm()
    return render(request, "bibliotheque/add.html", {"form": form})


def contact(request):

    if request.method == "POST":
        form_contact = ContactForm(request.POST)
        if form_contact.is_valid():
            print(form_contact.cleaned_data)
    else:
        form_contact = ContactForm()

    return render(request, "bibliotheque/contact.html", {"form": form_contact})


def html(request):
    return render(request, "bibliotheque/book_space/html.html")


def html3(request):
    return render(request, "bibliotheque/book_space/html3.html")
