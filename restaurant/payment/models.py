from django.db import models
from order.models import Order

# Create your models here.
class Payment(models.Model):
    order = models.OneToOneField(Order , on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
           ], default='pending')
    transaction_id = models.CharField(max_length=100,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"Payment for Order {self.order.id} - {self.status}"
