from django.db import models


class BikeStyle(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class BikeModel(models.Model):
    MAKE = 1
    FAMILY = 2
    MODEL = 3
    TYPE_CHOICES = (
        (MAKE, 'Make'),
        (FAMILY, 'Family'),
        (MODEL, 'Model'),
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES)
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class BikePart(models.Model):
    HANDLEBARS = 1
    PIPES = 2
    SEATS = 3
    WHEELS = 4
    CARGO = 5
    INTAKE = 6
    TANK = 7
    TYPE_CHOICES = (
        (HANDLEBARS, 'Handlebars'),
        (PIPES, 'Pipes'),
        (SEATS, 'Seats'),
        (WHEELS, 'Wheels'),
        (CARGO, 'Cargo'),
        (INTAKE, 'Intake'),
        (TANK, 'Tank'),
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES)
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Bike(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=128)
    image_url = models.URLField(max_length=256)
    styles = models.ManyToManyField(BikeStyle)
    models = models.ManyToManyField(BikeModel)

    def __str__(self):
        return self.name
