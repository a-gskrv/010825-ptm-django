from typing import Any

from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView

from my_app.models import Author
from my_app.serializers import AuthorDetailSerializer, AuthorListSerializer


class AuthorListGenericView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorListSerializer

    def get_serializer_context(self) -> dict[str, Any]:
        context: dict[str, Any] = super().get_serializer_context()

        context['include-related'] = self.request.query_params.get(
            'include-related', 'false'
        ).lower() == 'true'  # True | False

        return context


class AuthorRetrieveUpdateDestroyGenericView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorDetailSerializer

    lookup_field = 'username'  # поиск по колонке из БД
    lookup_url_kwarg = 'author'
