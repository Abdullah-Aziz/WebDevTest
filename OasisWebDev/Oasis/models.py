from django.db import models


class Products(models.Model):
    SKU = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200, null=True)
    QTY = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
