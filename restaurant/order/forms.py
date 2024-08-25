from django import forms
from .models import Order, OrderItem
from menu.models import MenuItem

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['menu_item', 'quantity']

class OrderForm(forms.ModelForm):
    items = forms.ModelMultipleChoiceField(queryset=MenuItem.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Order
        fields = ['items']
