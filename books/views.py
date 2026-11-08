from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('-created_at')
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']

    @action(detail=False, methods=['get'])
    def available(self, request):
        books = Book.objects.filter(available=True).order_by('-created_at')
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)