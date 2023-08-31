from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        ordering : ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.CharField(max_length=25)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    user_id = models.IntegerField(default=1)
    selled = models.BooleanField(default=False)
    buyer_id = models.IntegerField(null=True)

    def __str__(self):
        return self.name    


  


