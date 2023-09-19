from django.shortcuts import render
from django.http import Http404

from bookcrossing_project.data import BOOKS, CATEGORIES


def index_views(request):
    template_name = 'catalog/index.html'
    return render(request, template_name, {'books': BOOKS})


def book_views(request, id):
    template_name = 'catalog/book.html'
    try:
        book = {book['id']: book for book in BOOKS}[id]
    except KeyError:
        raise Http404('Такой книги не существует.')
    return render(request, template_name, {'book': book})


def categories_views(request):
    template_name = 'catalog/categories.html'
    return render(request, template_name, {'categories': CATEGORIES})


def category_views(request, category_str):
    template_name = 'catalog/category.html'
    category_book = []
    for book in BOOKS:
        if category_str in book["category"]:
            category_book.append(book)

    return render(request, template_name, {'category_book': category_book})

