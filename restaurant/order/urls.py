from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_order, name='create-order'),
    path('<int:order_id>/', views.order_detail, name='order-detail'),
    path('', views.order_list, name='order-list'),
]