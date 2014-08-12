from django.db import models
from datetime import date, datetime

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField()
    school = models.CharField(max_length=16, null=True)
    country = models.CharField(max_length=2, null=True)

    @property
    def full_name(self):
        return u'{0} {1}'.format(self.first_name, self.last_name)

    @property
    def age(self):
        today = date.today()
        return today.year - self.birthdate.year - ((today.month, today.day) \
            < (self.birthdate.month, self.birthdate.day))

    def __unicode__(self):
        return self.full_name

    class Meta:
        abstract = True
        ordering = ['first_name', 'last_name']

class Player(Person):
    jersey = models.PositiveSmallIntegerField(max_length=2)
    position = models.IntegerField(max_length=1)
    active = models.BooleanField()
    height = models.PositiveSmallIntegerField(verbose_name='Height (in)', max_length=2)
    weight = models.PositiveSmallIntegerField(verbose_name='Weight (lb)', max_length=3)

