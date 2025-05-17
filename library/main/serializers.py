from rest_framework import serializers
from .models import Book, Order


class BookSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Book.
    Возвращает все поля модели.
    В представлении добавляет поле
    'orders_count' — количество заказов на книгу.
    """

    class Meta:
        model = Book
        fields = '__all__'  # все поля модели Book

    def to_representation(self, instance):
        """
        Переопределение вывода данных.
        Добавляет количество заказов для книги.
        """
        representation = super().to_representation(instance)
        # Доп задание: количество заказов для этой книги
        representation['orders_count'] = instance.order_set.count()
        return representation


class OrderSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Order.
    Возвращает все поля модели.
    В представлении заменяет список ID книг на их подробные данные.
    """

    class Meta:
        model = Order
        fields = '__all__'  # Все поля модели Order

    def to_representation(self, instance):
        """
        Переопределение вывода данных.
        Вместо ID книг возвращает их поля: id, author, title, year.
        """
        representation = super().to_representation(instance)
        # Доп задание: вместо ID книг — полная информация о них
        books_data = []
        for book in instance.books.all():
            books_data.append({
                'id': book.id,
                'author': book.author,
                'title': book.title,
                'year': book.year,
            })
        representation['books'] = books_data
        return representation
