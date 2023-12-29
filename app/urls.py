from django.urls import path
from .views import AuthorListCreateView, AuthorDetailsView, BookListCreateView, BookDetailsView

urlpatterns = [
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorDetailsView.as_view(), name='author-details'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailsView.as_view(), name='book-details'),
]
