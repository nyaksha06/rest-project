from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', include('menu.urls')),
    path('order/', include('order.urls')),
    path('payment/', include('payment.urls')),
]
