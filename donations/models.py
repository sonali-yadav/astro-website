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

    def __str__(self):
        return self.title
