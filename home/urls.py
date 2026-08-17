from django.urls import path
from . import views

urlpatterns = [
    path("", views.menu, name="menu"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("order-confirmation/",views.order_confirmation,name="order_confirmation"),
   
    path("save-orders/",views.save_orders,name="save_orders"),
    path("login/",views.login_view,name="login"),
    path("logout/",views.logout_view,name="logout"),
    path("orders/",views.orders,name="orders"),
]
