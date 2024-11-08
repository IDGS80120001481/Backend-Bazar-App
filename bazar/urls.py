from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/items', views.search_product),
    path('api/items/<int:id>', views.get_detail),
    path('api/addSale', views.add_sale),
    path('api/sales', views.get_sales),
]