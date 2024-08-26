from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:order_id>/', views.create_payment, name='create-payment'),
    path('success/<int:order_id>/', views.payment_success, name='payment-success'),
    path('failed/<int:order_id>/', views.payment_failed, name='payment-failed'),
]
