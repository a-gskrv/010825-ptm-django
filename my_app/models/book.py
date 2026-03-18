from django.core.validators import MinLengthValidator
from django.db import models


class Book(models.Model):  # table name like <app_name>_<model_name>
    class Genre(models.TextChoices):
        FANTASY = 'Fantasy', 'FANTASY CATEGORY'
        MYSTIC = 'Mystic', 'MYSTIC CATEGORY'
        BIOGRAPHY = 'Biography', 'BIOGRAPHY CATEGORY'
        SCIENCE = 'Science', 'SCIENCE CATEGORY'
        FICTION = 'Fiction', 'FICTION CATEGORY'
        SCIENCE_FICTION = 'Science Fiction', 'SCIENCE FICTION CATEGORY'
        HORROR = 'Horror', 'HORROR CATEGORY'
        DETECTIVE = 'Detective', 'DETECTIVE CATEGORY'
        ROMANCE = 'Romance', 'ROMANCE CATEGORY'
        N_A = 'N/A', 'UNRECOGNISED CATEGORY'

    title = models.CharField(
        max_length=125,
        unique=True,
        verbose_name="Название книги",
        error_messages={  #  пересмотреть настройку параметра
            'blank': 'Сожалеем, но книгу нельзя создать без названия книги.',
            'unique': 'Кажется книга с таким названием уже существует.',
        }
    )
    description = models.TextField(
        verbose_name="Описание книги",
        validators=[
            MinLengthValidator(20),
            # MaxLengthValidator(500)
        ]
    )
    comment = models.TextField(
        null=True,
        blank=True,
        # unique_for_date='published_date'
        # unique_for_month='published_date'
        # unique_for_year='published_date'
    )
    published_date = models.DateTimeField(verbose_name="Дата публикации")
    price = models.DecimalField(  # 123.45
        verbose_name="Цена книги",
        help_text="Цена книги в евро. Должно быть больше 0",
        max_digits=5,
        decimal_places=2,
        null=True,  #  сторона базы данных
        blank=True  #  сторона админ панели
    )
    discounted_price = models.DecimalField(  # 123.45
        verbose_name="Цена книги со скидкой",
        help_text="Цена книги в евро. Должно быть больше 0",
        max_digits=5,
        decimal_places=2,
        null=True,  #  сторона базы данных
        blank=True  #  сторона админ панели
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="books"
    )
    genre = models.CharField(
        max_length=30,
        choices=Genre,
        default=Genre.N_A
    )
    is_bestseller = models.BooleanField(default=False)
    pages = models.PositiveSmallIntegerField(
        null=True,
        blank=True
    )
    publisher = models.ForeignKey(
        'User',
        on_delete=models.SET_NULL,
        related_name="published_books",
        null=True,
        blank=True
    )
    author = models.ForeignKey(
        'Author',
        on_delete=models.SET_NULL,
        related_name="books",
        null=True,
        blank=True
    )

    def __str__(self):
        # return self.title
        return f"{self.title} ({self.published_date})   --- {self.id}"

    # def __str__(self):
    #     return str(self)


    class Meta:
        db_table = "books"  # своё имя таблицы в БД

        verbose_name = "Book"  # человекочитабельное название класса (ед. число)
        verbose_name_plural = "Books"  # человекочитабельное название класса (множ. число)
        ordering = ["-published_date", "title"]  # desc
        # ordering = ["published_date",]  # asc

        indexes = [
            models.Index(
                fields=["title", "category"],
                name="book_title_category_idx"
            )
        ]

        constraints = [
            models.UniqueConstraint(
                fields=["title", "category"],
                name="book_title_category_unq_cst"
            )
        ]

        # abstract = True
        # default_related_name = "books"

        get_latest_by = "-published_date"
