from django.core.validators import MinLengthValidator
from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=200
    )
    content = models.TextField(
        validators=[
            MinLengthValidator(50)
        ]
    )

    # One to Many RelationShip
    author = models.ForeignKey(
        'User',
        # on_delete=models.DO_NOTHING,  # при удалении родителя ничего не делай
        # on_delete=models.CASCADE,  # при удалении родителя удаляй все связанные записи КАСКАДНО
        on_delete=models.SET_NULL,  # обязательно требует включение null=True. При удалении родителя устанавливай значение NULL для всех его дочерних объектов
        # on_delete=models.SET_DEFAULT,  # обязательно требует включение default=<default value>. При удалении родителя устанавливай значение по умолчанию для всех его дочерних объектов
        # on_delete=models.PROTECT  # запретить удаление родителя, пока на него есть ХОТЬ ОДНА ССЫЛКА
        null=True,
        blank=True,
        related_name='posts'
    )
    moderated = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    def __str__(self):
        author = self.author.username if self.author else "Unknown author"

        return f"{self.title} Publisher: ({author})"

    class Meta:
        db_table = "posts"
        ordering = ["-created_at"]


# Post.author -> -> Author obj.
# Author.posts -> ->  [Post obj, ... Post obj]
