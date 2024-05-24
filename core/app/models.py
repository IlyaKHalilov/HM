from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=123)
    price = models.FloatField()
    description = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='media/products')

    def __str__(self):
        return self.title
