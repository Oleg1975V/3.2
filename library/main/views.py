from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Book, Order
from main.serializers import BookSerializer, OrderSerializer


@api_view(['GET'])
def books_list(request):
    """
    Получает список всех книг из базы данных.

    Возвращает JSON-ответ с сериализованным списком книг.
    """
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


class CreateBookView(APIView):
    """
    Представление для создания новой книги через POST-запрос.
    """

    def post(self, request):
        """
        Обрабатывает POST-запрос на создание книги.

        Если данные валидны — сохраняет книгу в базе данных.
        """
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Книга успешно создана')


class BookDetailsView(RetrieveAPIView):
    """
    Представление для получения информации о конкретной книге.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateView(UpdateAPIView):
    """
    Представление для частичного или полного обновления данных о книге.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDeleteView(DestroyAPIView):
    """
    Представление для удаления книги.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления заказами (CRUD).
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
