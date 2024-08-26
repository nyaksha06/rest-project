from django.shortcuts import render, redirect
from .models import Order, OrderItem
from .forms import OrderForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'order/index.html')


@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in form.cleaned_data['items']:
                OrderItem.objects.create(
                    order=order,
                    menu_item=item['menu_item'],
                    quantity=item['quantity'],
                    price=item['menu_item'].price
                )
            return redirect('order-detail', order_id=order.id)
    else:
        form = OrderForm()
    return render(request, 'order/create_order.html', {'form': form})



@login_required
def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'order/order_detail.html', {'order': order})


@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order/order_list.html', {'orders': orders})