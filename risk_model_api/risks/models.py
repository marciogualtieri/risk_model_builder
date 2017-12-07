from django.db import models
from django.core.exceptions import ValidationError

class Risk(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def validate(self):
        for field in self.fields.all():
            field.validate()

    def __str__(self):
        return 'name="{}" description="{}"'.format(self.name, self.description)

    class Meta:
        unique_together = ["name"]

class Field(models.Model):

    TYPE_CHOICES = (('text', 'Plain Text'), ('number', 'Number'), ('date', 'Date'), ('enum', 'Enumeration'))

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    description = models.TextField(blank=True)
    risk = models.ForeignKey(Risk, related_name='fields', null=True, on_delete=models.CASCADE)

    def validate(self):
        choices = len(self.choices.all()) 
        if self.type == 'enum' and choices < 2:
            raise ValidationError("Field \"%s\" is type enum and requires two or more choices." % self.name)
        if self.type != 'enum' and choices != 0:
            raise ValidationError("Field \"%s\" is type %s and doesn't support choices." % (self.name, self.type))

    def __str__(self):
        return 'name="{}" type="{}" description="{}"'.format(self.name, self.type, self.description)


class Choice(models.Model):

    choice = models.CharField(max_length=200)
    field = models.ForeignKey(Field, related_name='choices', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return 'choice="{}"'.format(self.choice)