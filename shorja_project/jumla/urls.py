from django.contrib import admin
from django.urls import path, include
from .views import *

# urls
urlpatterns = [
    path('', shopper.home, name="home"),
    # path('',  HomePageView.as_view(), name="home"),
    path('Account/', include([

        path('register/', Account.register_view, name="register"),
        path('login/', Account.login_view, name="login"),
        # path('', include('django.contrib.auth.urls')),
        path('logout/', Account.logout_view, name="logout"),
        path('change_password/', Account.change_password, name="change_password"),
    ])),
    path('shopper/', include([
        path('brows_bills', shopper.show_cart_bills_order, name="brows_bills"),
        path('who_are_we', shopper.who, name='who_are_we'),
        path('services', shopper.services, name='services'),
        path('show_markets', shopper.show_markets, name='show_markets'),
        # APIs
        path('add-to-cart', shopper.add_to_cart, name="add_to_cart"),
        path('update_quentity', shopper.update_quentity, name="update_quentity"),
        path('check_item_in_bill_order', shopper.check_item_in_bill_order, name="check_item_in_bill_order"),
         path('polls' , shopper.polls, name = 'polls' ),
        path('Vote/<str:pk>' , shopper.Vote , name = 'Vote'),
    ])),
    path('vendor/', include([
        path('', vender.vendor_home, name='vendor_home'),
        path('create_product', vender.create_new_product, name='create_product'),
        path('update_product/<product_id>/', vender.update_product, name='update_product'),
        path('view_customer_bills/', vender.view_customer_bills, name='view_customer_bills'),
        path('view_bill_products/<bill_id>/', vender.view_bill_products, name='view_bill_products'),
        path('store/<store>/', vender.show_store, name='show_store'),
        # Api
        path('delete_product', vender.delete_product_and_update_is_active, name='delete_product'),
       
        path('Result/<str:pk>', vender.Result , name = 'Result'),
      
    ])),
    path('delivery/', include([
        path('', delivery.home, name='delivery_home'),
        path('get_cart_bills/<cart_id>', delivery.get_cart_bills, name='get_cart_bills'),
    ])),

]

