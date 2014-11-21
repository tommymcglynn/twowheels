from django.db import models


class BikeStyle(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class BikeMake(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class BikeFamily(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=64)
    make = models.ForeignKey(BikeMake)

    class Meta:
        unique_together = ("make", "name")

    def __str__(self):
        return '%s %s' % (self.make, self.name)


class BikeModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=64)
    family = models.ForeignKey(BikeFamily)

    class Meta:
        unique_together = ("family", "name")

    def __str__(self):
        return '%s %s' % (self.family, self.name)


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
    source_url = models.URLField(max_length=256, null=True)
    model = models.ForeignKey(BikeModel)
    parts = models.ManyToManyField(BikePart, related_name='parts', blank=True)
    styles = models.ManyToManyField(BikeStyle, related_name='styles')

    def __str__(self):
        return self.name

    def image_tag(self):
        return u'<img src="%s" style="max-width: 200px;" />' % self.image_url
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
