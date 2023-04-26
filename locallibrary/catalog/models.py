from django.db import models
class Genre(models.Model):
    name = models.CharField(
        max_length = 200,
        help_text = "Enter a book genre"
    )

    def __str__(self):
        return self.name

from django.urls import reverse
class Book(models.Model):
    title = models.CharField(
        max_length = 200
    )
    
    author = models.ForeignKey(
        'Author',
        on_delete = models.SET_NULL,
        null = True
    )

    summary = models.TextField(
        max_length = 1000,
        help_text = "Enter a brief book summary",
    )

    isbn = models.CharField(
        'ISBN',
        max_length = 13,
        unique = True
    )

    genre = models.ManyToManyField(
        Genre,
        help_text = "Select a book genre"
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'book-detail',
            args = [str(self.id)]
        )

import uuid
class BookInstance(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        help_text = "Unique ID for this particular book"
    )

    book = models.ForeignKey(
        'Book',
        on_delete = models.RESTRICT,
        null = True
    )

    language = models.ForeignKey(
        'Language',
        on_delete = models.RESTRICT,
        null = True
    )

    imprint = models.CharField(
        max_length = 200
    )

    due_back = models.DateField(
        null = True,
        blank = True
    )

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Reserved')
    )

    status = models.CharField(
        max_length = 1,
        choices = LOAN_STATUS,
        blank = True,
        default = 'm',
        help_text = "Book Availablity"
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'

class Author(models.Model):
    first_name = models.CharField(
        max_length = 100
    )

    last_name = models.CharField(
        max_length = 100
    )

    date_of_birth = models.DateField(
        null = True,
        blank = True
    )

    date_of_death = models.DateField(
        'Died',
        null = True,
        blank = True
    )

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse(
            'author-detail',
            args = [str(self.id)]
        )

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

class Language(models.Model):
    name = models.CharField(
        max_length = 20
    )

    def __str__(self):
        return self.name