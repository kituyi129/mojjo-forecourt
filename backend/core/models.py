from django.db import models

class Products(models.Model):
    Title=models.CharField(max_length=200)
    Slug=models.SlugField(unique= True, blank=False)
    image=models.ImageField("products", blank=True, unique=False)
    Description = models.TextField(blank=True)
    Price =models.DecimalField(max_digits=10, decimal_places=2)
    Stock =models.PositiveIntegerField(default =0)
    is_active =models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)
   
   
    def __str__(self):
        return f"{self.Title} - Stocks:-{self.Stock}"