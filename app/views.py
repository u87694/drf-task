from rest_framework import generics, serializers
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorListCreateView(generics.ListCreateAPIView):
    """List all Authors or create new Author"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailsView(generics.RetrieveAPIView):
    """Retrieve details of a specific Author by ID"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookListCreateView(generics.ListCreateAPIView):
    """List all Books or create new Book"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        author_id = self.request.data.get('author')
        author = get_object_or_404(Author, id=author_id)

        if author.book_set.count() >= 5:
            # raise Validation error as having more than 5 books per author is not valid
            raise serializers.ValidationError(
                {"error": "An author cannot have more than 5 books."}
            )

        serializer.save()

class BookDetailsView(generics.RetrieveAPIView):
    """Retrieve details of a specific Book by ID"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
