from django.db import models
from django.core.exceptions import ValidationError


class Risk(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ["name"]


class Field(models.Model):

    TYPE_CHOICES = (('text', 'Plain Text'), ('number', 'Number'), ('date', 'Date'), ('enum', 'Enumeration'))

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    description = models.TextField(blank=True)
    risk = models.ForeignKey(Risk, related_name='fields', null=True, on_delete=models.CASCADE)


class Choice(models.Model):

    choice = models.CharField(max_length=200)
    field = models.ForeignKey(Field, related_name='choices', null=True, on_delete=models.CASCADE)