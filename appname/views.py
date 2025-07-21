from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db import models

from .models import Product
from .forms import SignupForm
from .models import Order




# ----------------------------
# Authentication Views
# ----------------------------

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# ----------------------------
# Main Views
# ----------------------------

@login_required
def index_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def compare_view(request):
    return render(request, 'compare.html')

def warranty_view(request):
    return render(request, 'warranty.html')

def store_locator_view(request):
    return render(request, 'store_locator.html')

def theme_toggle_view(request):
    return render(request, 'theme_toggle.html')

def cart_view(request):
    cart = request.session.get('cart', {})
    return render(request, 'cart.html', {'cart': cart})

# ----------------------------
# Product Category Views
# ----------------------------

def smartphone_view(request):
    return render(request, 'smartphone.html')

def laptop_view(request):
    return render(request, 'laptop.html')

def smartwatch_view(request):
    return render(request, 'smartwatch.html')

def accessories_view(request):
    return render(request, 'accessories.html')

def audio_view(request):
    return render(request, 'audio.html')

def gaming_view(request):
    return render(request, 'gaming.html')

def checkout_view(request):
    return render(request, 'checkout.html')

# ----------------------------
# Individual Product Pages
# ----------------------------

def products_view(request):
    return render(request, 'products.html')

def product1_view(request):
    return render(request, 'product1.html')

def product2_view(request):
    return render(request, 'product2.html')

def product3_view(request):
    return render(request, 'product3.html')

def product4_view(request):
    return render(request, 'product4.html')

def product5_view(request):
    return render(request, 'product5.html')

def product6_view(request):
    return render(request, 'product6.html')

def smartphone_product_view(request):
    return render(request, 'product_smartphone.html')

from django.shortcuts import render

def allproducts(request):
    products = [
        {"id": 1, "name": "iPhone 16 Pro Max", "price": 159900, "image": "assets/iPhone 16 Pro Max_ap.jpeg"},
        {"id": 2, "name": "Galaxy S25 Ultra", "price": 139900, "image": "assets/Samsung_Galaxy_s25_ap.jpeg"},
        {"id": 3, "name": "MacBook Pro M4", "price": 249900, "image": "assets/MacBook Pro M4_ap.jpg"},
        {"id": 4, "name": "Apple Watch X", "price": 99900, "image": "assets/Apple Watch X_ap.jpeg"},
        {"id": 5, "name": "MagSafe Case", "price": 6900, "image": "assets/magsafe-case.jpg"},
        {"id": 6, "name": "AirPods Max", "price": 59900, "image": "assets/AirPods Max_ap.jpeg"},
        {"id": 7, "name": "PlayStation 6", "price": 74900, "image": "assets/PlayStation 6_ap.jpg"},
        {"id": 8, "name": "iPad Pro M3", "price": 129900, "image": "assets/iPad Pro M3_ap.jpeg"},
        {"id": 9, "name": "Surface Laptop 6", "price": 114999, "image": "assets/Surface Laptop 6_ap.jpg"},
        {"id": 10, "name": "Sony WH-1000XM6", "price": 32990, "image": "assets/Sony WH-1000XM6_ap.jpeg"},
        {"id": 11, "name": "Google Pixel 9 Pro", "price": 99999, "image": "assets/Google Pixel 9 Pro_ap.jpg"},
        {"id": 12, "name": "Asus ROG Phone 8", "price": 79999, "image": "assets/Asus ROG Phone 8.png"},
        {"id": 13, "name": "Alienware Aurora R16", "price": 329990, "image": "assets/Alienware Aurora R16_ap.jpg"},
        {"id": 14, "name": "DJI Mini 4 Pro Drone", "price": 89999, "image": "assets/DJI Mini 4 Pro Drone_ap.jpeg"},
        {"id": 15, "name": "Oculus Quest 3", "price": 59990, "image": "assets/Oculus Quest 3_ap.jpeg"},
        {"id": 16, "name": "Bose Smart Ultra Soundbar", "price": 114900, "image": "assets/Bose Smart Ultra Soundbar_ap.jpg"},
        {"id": 17, "name": "Samsung 8K QLED TV 75”", "price": 324999, "image": "assets/Samsung 8K QLED TV 75”_ap.jpeg"},
        {"id": 18, "name": "Apple Vision Pro", "price": 349900, "image": "assets/Apple Vision Pro_ap.jpeg"},
        {"id": 19, "name": "Nothing Phone 3", "price": 49999, "image": "assets/Nothing Phone 3_ap.jpg"},
        {"id": 20, "name": "Steam Deck OLED", "price": 69999, "image": "assets/Steam Deck OLED_ap.jpeg"},
    ]
    return render(request, 'allproducts.html', {'products': products})

def view_carts(request):
    return render(request, 'carts.html')


def all_products(request):
    products = Product.objects.all()
    return render(request, 'allproducts.html', {'products': products})

def checkout(request):
    if request.method == 'POST':
        order = Order(
            full_name = request.POST.get('full_name'),
            email = request.POST.get('email'),
            address = request.POST.get('address'),
            city = request.POST.get('city'),
            state = request.POST.get('state'),
            postal_code = request.POST.get('postal_code'),
            cardholder_name = request.POST.get('cardholder_name'),
            card_number = request.POST.get('card_number'),
            expiry_date = request.POST.get('expiry_date'),
            cvv = request.POST.get('cvv')
        )
        order.save()
        return redirect('purchase_success')

    return render(request, 'checkout.html')



def purchase_success(request):
    return render(request, 'purchase_success.html')

def view_wishlist(request):
    return render(request, 'wishlist.html')