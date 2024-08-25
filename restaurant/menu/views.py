from django.shortcuts import render
from .models import Category, MenuItem

def index(request):
    return render(request, 'menu/index.html')


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'menu/category_list.html' , {'categories' : categories})



def menu_items_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    menu_items = MenuItem.objects.filter(category=category)
    return render(request, 'menu/menu_items_by_category.html',{'category':category, 'menu_items':menu_items})



def menu_item_detail(request, item_id):
    menu_item = MenuItem.objects.get(id=item_id)
    return render(request, 'menu/menu_item_detail.html',{'menu_item':menu_item})