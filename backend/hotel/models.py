from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=150)
    slag = models.SlugField(max_length=150,unique=True)

    def __str__(self) -> str:
        return self.category_name

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=150)
    discription = models.TextField()
    adress = models.CharField(max_length=150)
    klass = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/',blank=True,null=True)
    image3 = models.ImageField(upload_to='images/',blank=True,null=True)

    def __str__(self) -> str:
        return self.hotel_name