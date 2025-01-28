from django.template.defaultfilters import title
from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'content', 'author', 'isbn', 'price')

    def validate(self, data):
        title = data['title']
        author = data['author']
        if not title.isalpha():
            raise serializers.ValidationError({
                "status": False,
                "message": "Kitobni sarlavhasi harflardan tashkil topgan bo'lishi kerak!",
            })

        if Book.objects.filter(title = title, author = author).exists():
            raise serializers.ValidationError({
                "status": False,
                "message": "Kitob sarlovhasi va muallifi bir xil bo'lgan kitob yuklay olmaysiz",
            })

        return data

    def validate_price(self, price):
        if price <= 0 or price > 99999999:
            raise serializers.ValidationError({
                "status": False,
                "message": "Narx xato kiritilgan",
            })
        return price

# class BookSerializer(serializers.Serializer)
