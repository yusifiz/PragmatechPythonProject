from django.db import models

# Create your models here.

class Product(models.Model):
    COLORS = {
        (1,'black'),
        (2,'yellow'),
        (3,'red')
    }

    name = models.CharField(max_length=200, help_text='Enter Product Name')
    color  = models.SmallIntegerField(max_length=100,choices=COLORS)
    price = models.SmallIntegerField(default=1)

    def __str__(self):
        return self.name