from rest_framework import serializers

from my_app.models import Author


class AuthorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'id',
            'last_name'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if self.context.get('include-related'):
            representation['published_books'] = [
                {
                    "id": book.id,
                    "title": book.title,
                    "published_date": book.published_date,
                }
                for book in instance.books.all()
            ]

        return representation