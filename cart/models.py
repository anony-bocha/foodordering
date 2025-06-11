from django.db import models
from products.models import Product

class CartItem(models.Model):
    session_key = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.product_price * self.quantity

    def __str__(self):
        return f"{self.product.product_name} ({self.quantity})"
