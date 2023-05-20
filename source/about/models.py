from django.db import models
from phonenumber_field.modelfields import (  # pyright: ignore[reportMissingTypeStubs]
    PhoneNumberField,
)


class Experience(models.Model):

    title = models.CharField(max_length=30)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.title}'


class Person(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    phone_number = PhoneNumberField

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
