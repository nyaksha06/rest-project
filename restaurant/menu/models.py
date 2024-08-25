from django.db import models

# Create your models here.

class Catagory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank = True , null = True)

    def __str__(self):
        return self.name
    


class MenuItem(models.Model):
    catagory = models.ForeignKey(Catagory , on_delete= models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank = True , null = True)
    price = models.DecimalField(max_digits =6, decimal_places=2)
    available = models.BooleanField(default = True)


    def __str__(self):
        return self.name
    
