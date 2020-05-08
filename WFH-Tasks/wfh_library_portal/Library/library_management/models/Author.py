from django.db import models


class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "Authors"
        verbose_name_plural = "Authors"

    def __str__(self):
        return '{0}, {1}'.format(self.first_name, self.last_name)

