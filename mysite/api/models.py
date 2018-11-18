from django.db import models
from django.urls import reverse


class PersonInfo(models.Model):
    Description = models.TextField(
        null=True
    )
    FirstName = models.TextField()
    MiddleName = models.TextField(
        null=True
    )
    LastName = models.TextField()
    Phone = models.TextField(
        null=True
    )
    Birthday = models.DateField(
        null=True
    )
    HaveChildren = models.BooleanField(
        default=False,
        null=False
    )
    Position = models.ForeignKey('Position', on_delete=models.PROTECT,
                                 null=True)
    Country = models.TextField(
        null=True
    )
    City = models.TextField(
        null=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('person_edit', kwargs={'pk': self.pk})


class Position(models.Model):
    Name = models.TextField()