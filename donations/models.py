from django.db import models


class Yajnas(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    amount = models.IntegerField()
    thumbnail = models.ImageField(upload_to='media', blank=True)

    def __str__(self):
        return self.title


class Mantras(models.Model):
    title = models.CharField(max_length=100)
    small_don = models.IntegerField()
    vedic_don = models.IntegerField()
    basic = models.CharField(max_length=50, default="")
    note = models.CharField(max_length=150, default="")
    qualities = models.CharField(max_length=250, default="")

    def __str__(self):
        return self.title


class Rudraksh(models.Model):
    title = models.CharField(max_length=50, default="")
    price = models.IntegerField()
    planet = models.CharField(max_length=10, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.title


class RudTable(models.Model):
    moon_sign = models.CharField(max_length=25, default="")
    prescribed = models.CharField(max_length=50, default="")
    prohibited = models.CharField(max_length=25, default="")
    planets = models.CharField(max_length=30, default="")
