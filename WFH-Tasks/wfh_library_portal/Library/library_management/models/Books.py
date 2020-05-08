from django.db import models
from library_management.models import Author


class Books(models.Model):
    """Model representing Books."""
    isbn = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genere = models.CharField(max_length=20)
    available = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Books and Authors"
        verbose_name_plural = "Books"

    def __str__(self):
        return '{0}, {1}'.format(self.title, self.author)
        