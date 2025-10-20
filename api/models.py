from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(to=Category,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    img = models.ImageField(upload_to='products/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name