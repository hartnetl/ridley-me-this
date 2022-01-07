from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Turtles(models.Model):
    class Meta:
        verbose_name_plural = 'Turtles'

    SPECIES = [
        ('logger', 'Loggerhead'),
        ('green', 'Green'),
        ('leather', 'Leatherback'),
        ('flat', 'Flatback'),
        ('hawks', 'Hawksbill'),
        ('olive', 'Olive Ridley'),
        ("kemp", "Kemp's Ridley"),
    ]

    title = models.CharField(max_length=254)
    turtle_id = models.CharField(max_length=6)
    name = models.CharField(max_length=30, blank=True, null=True)
    species = models.CharField(choices=SPECIES, max_length=10)
    description = models.TextField()
    date_tagged = models.DateField(auto_now=False, auto_now_add=False)
    location_tagged = CountryField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sponsored_status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title


class turtle_sponsor(models.Model):
    class Meta:
        verbose_name_plural = 'Turtle Sponsorships'

    category = models.ForeignKey('merchandise.Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    turtle = models.ForeignKey('Turtles', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=30)
    sponsorship_start = models.DateField(auto_now=False, auto_now_add=False)
    sponsorship_end = models.DateField(auto_now=False, auto_now_add=False)
    sponsored_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
