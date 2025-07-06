from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/products/', include('products.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/carts/', include('carts.urls')),             
    path('api/categories/', include('products.urls')),   
    path('api/wishlist/', include('wishlist.urls')),       
    path('api/notifications/', include('notifications.urls')),  
   
]