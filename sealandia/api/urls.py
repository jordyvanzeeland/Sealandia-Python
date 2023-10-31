from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from .views import *
from .modules.auth import *
from .modules.books import *

urlpatterns = [
    # Login
    path('auth/login', csrf_exempt(login)),

    # Books
    path('books/all', getAllBooks),
    path('books/years', getYears),
    path('books/genres', books_per_genre_per_month),
    path('books/genres/count', countGenres),
    path('books/ratings', avg_ratings_per_month),
    path('books/ratings/count', countRatings),
    path('books/authors', books_per_author),
    path('books/countries', books_per_country),
    path('books/insert', addBook),
    path('books/delete', deleteBook),
    path('books/update', updateBook),
]