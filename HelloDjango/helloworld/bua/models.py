from django.db import models
# Create your models here.
class Cart(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)
    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=False, null=False)
    def __str__(self):
        return self.name
