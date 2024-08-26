from django.conf import settings
from django.shortcuts import render, redirect
from paypalrestsdk import Payment
from order.models import Order
from .models import Payment as PaymentModel

def index(request):
    return render(request, 'order/index.html')


def create_payment(request, order_id):
    order = Order.objects.get(id = order_id)
    payment = Payment({
        "intent": "sale",
        "payer": {"payment_method": "paypal"},
        "redirect_urls": {
            "return_url": request.build_absolute_uri('/payments/success/'),
            "cancel_url": request.build_absolute_uri('/payments/cancel/'),
        },
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": f"Order {order.id}",
                    "sku": "001",
                    "price": str(order.total_price),
                    "currency": "USD",
                    "quantity": 1
                }]
            },
            "amount": {
                "total": str(order.total_price),
                "currency": "USD"
            },
            "description": f"Payment for Order {order.id}"
        }]
    })

    if payment.create():
        for link in payment.links:
            if link.rel == "approval_url":
                approval_url = str(link.href)
                break
        return redirect(approval_url)
    else:
        return redirect('payment-failed', order_id=order.id)
    




def payment_success(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'payments/payment_success.html', {'order': order})



def payment_failed(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'payments/payment_failed.html', {'order': order})


