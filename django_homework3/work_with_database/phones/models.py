from django.db import models as md


class Phone(md.Model):
    name = md.TextField()
    price = md.FloatField()
    image = md.TextField()
    release_date = md.DateField()
    lte_exists = md.BooleanField()
    slug = md.SlugField()

    def __str__(self):
        return f'{self.id}: {self.name}'
