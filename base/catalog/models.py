from django.db import models

# models for the brands
class Brand(models.Model):
    name = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

#models for the Product
class Product(models.Model):
    sku = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    visit = models.IntegerField(default=0)
    brand = models.ForeignKey(Brand,on_delete=models.RESTRICT)
    
    def __str__(self):
        return self.name
    