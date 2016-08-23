from __future__ import unicode_literals
from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return '{}'.format(self.name)


class Ability(models.Model):

    name = models.CharField(max_length=32)
    _type = models.ForeignKey('pokedex.Type', related_name='abilities')
    effect = models.CharField(max_length=32)

    def __str__(self):
        return '{}'.format(self.name)


class Pokemon(models.Model):
    GENDERS = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    name = models.CharField(max_length=32)
    gender = models.CharField(choices=GENDERS, max_length=16, null=True, blank=True)
    weight = models.PositiveSmallIntegerField(default=0)
    _type = models.ForeignKey('pokedex.Type', related_name='pokemon', null=True, blank=True)
    abilities = models.ManyToManyField('pokedex.Ability', related_name='abilities', blank=True)

    def __str__(self):
        return '{}'.format(self.name)
