from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('index/')),         

    # Authentication
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    # Main Pages
    path('index/', views.index_view, name='index'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('compare/', views.compare_view, name='compare'),
    path('warranty/', views.warranty_view, name='warranty'),
    path('store_locator/', views.store_locator_view, name='store_locator'),
    path('theme_toggle/', views.theme_toggle_view, name='theme_toggle'),

    # Product Categories
    path('smartphone/', views.smartphone_view, name='smartphone'),
    path('laptop/', views.laptop_view, name='laptop'),
    path('smartwatch/', views.smartwatch_view, name='smartwatch'),
    path('accessories/', views.accessories_view, name='accessories'),
    path('audio/', views.audio_view, name='audio'),
    path('gaming/', views.gaming_view, name='gaming'),

    # Products and Cart
    path('products/', views.products_view, name='products'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout_view, name='checkout'),

    # Static Product Pages (Optional — if you want specific hard-coded views)
    path('product1/', views.product1_view, name='product1'),
    path('product2/', views.product2_view, name='product2'),
    path('product3/', views.product3_view, name='product3'),
    path('product4/', views.product4_view, name='product4'),
    path('product5/', views.product5_view, name='product5'),
    path('product6/', views.product6_view, name='product6'),

    # Template test page (can be removed if unused)
    path('smartphone/product.html', views.smartphone_product_view),

    path('allproducts/', views.allproducts, name='allproducts'),
    path('carts/', views.view_carts, name='carts'),
    path('checkout/', views.checkout, name='checkout'),
    path('wishlist/', views.view_wishlist, name='view_wishlist'),


]