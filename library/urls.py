"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from my_app.views.books import (
    list_create_books,
    retrieve_update_destroy_book,
    BooksListAPIView
)

from my_app.views.categories import (
    CategoryListCreateAPIView,
    CategoryRetrieveUpdateDestroyAPIView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('books/', list_create_books),
    path('books/', BooksListAPIView.as_view()),
    path('books/<int:pk>', retrieve_update_destroy_book),
    path('categories/', CategoryListCreateAPIView.as_view()),
    path('categories/<int:pk>', CategoryRetrieveUpdateDestroyAPIView.as_view()),
]
