from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category-list'),
    path('category/<int:category_id>/', views.menu_items_by_category, name='menu-items-by-category'),
    path('item/<int:item_id>/', views.menu_item_detail, name='menu-item-detail'),
]
