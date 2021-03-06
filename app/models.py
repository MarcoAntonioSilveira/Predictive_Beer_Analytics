from django.db import models

class Word(models.Model):
    value = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=6,decimal_places=5)
    votes = models.IntegerField()

class Color(models.Model):
    value = models.CharField(max_length=20)
    rating = models.DecimalField(max_digits=6,decimal_places=5)
    votes = models.IntegerField()

class Location(models.Model):
    location = models.CharField(max_length=100)

class BeerStyle(models.Model):
    styleName = models.CharField(max_length=30)
    numRatings = models.BigIntegerField()


class AbvsRange(models.Model):
    range = models.CharField(max_length=100)

class StyleData(models.Model):
    location = models.ForeignKey(Location)
    beerStyle = models.ForeignKey(BeerStyle)
    latcoord = models.TextField(null=True, blank=True)
    lngcoord = models.TextField(null=True, blank=True)
    rating = models.TextField(null=True, blank=True)


class Abvs(models.Model):
    location = models.ForeignKey(Location)
    abvsrange = models.ForeignKey(AbvsRange)
    latcoord = models.TextField(null=True, blank=True)
    lngcoord = models.TextField(null=True, blank=True)
    rating = models.TextField(null=True, blank=True)

