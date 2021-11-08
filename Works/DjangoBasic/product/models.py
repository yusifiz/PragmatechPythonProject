from django.db import models

class Product(models.Model):
    COLORS = (
        (1, 'black'),
        (2, 'white'),
        (3, 'red')
    )
    name = models.CharField(max_length=200, help_text='Enter product name')
    color = models.IntegerField(choices=COLORS,)
    price = models.IntegerField(default=1)
    product_tag = models.ManyToManyField('Tag')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    title = models.CharField(max_length=63, null=True, blank=True)

    def __str__(self):
        return self.title