from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from .models import Product
from offer.models import Offer
from django.db.models import F
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == 'POST':
        str_username = request.POST.get('username')
        str_password = request.POST.get('password')
        user = auth.authenticate(username=str_username, password=str_password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Check your credentials')
            return redirect(login)
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        str_firstname = request.POST.get('firstname')
        str_lastname = request.POST.get('lastname')
        str_email = request.POST.get('email')
        str_username = request.POST.get('username')
        str_password = request.POST.get('password1')

        ins_user = User.objects.create_user(first_name=str_firstname, last_name=str_lastname, email=str_email, username=str_username, password=str_password)
        ins_user.save()
        print('user_created')
        return redirect('login')
    return render(request, 'register.html')


def home(request):
    ins_products = Offer.objects.annotate(strModel=F('fk_product__str_model'), strBrand=F('fk_product__str_brand'),
                                        intPrice=F('fk_product__int_price'), strRam=F('fk_product__str_ram'), strCamera=F('fk_product__str_camera'), intOfferPrice=F('int_offer_price'),
                                        intProductId=F('fk_product__id'))
    return render(request, 'home.html', {'products': ins_products})


def add_product(request):
    if request.method == 'POST':
        str_brand = request.POST.get('strBrand')
        str_model = request.POST.get('strModel')
        str_ram = request.POST.get('strRam')
        str_memory = request.POST.get('strMemory')
        str_camera = request.POST.get('strCamera')
        str_battery = request.POST.get('strBattery')
        str_processor = request.POST.get('strProcessor')
        int_price = int(request.POST.get('strPrice'))
        img_image = request.FILES.get('imgImage')
        
        ins_product = Product(str_brand=str_brand, str_model=str_model, str_ram=str_ram, str_memory=str_memory, str_camera=str_camera, str_battery=str_battery,
                                            str_processor=str_processor, int_price=int_price, img_image=img_image)
        ins_product.save()

        int_offer_price = int_price
        int_discount = (100-(int_offer_price//int_price)*100)
        ins_offer = Offer(fk_product=ins_product, int_offer_price=int_price, int_offer_percent=int_discount)
        ins_offer.save()
        return redirect('home')
    else:
        return render(request, 'add_product.html')


def view_product(request, int_id):
    ins_product = Product.objects.get(id=int_id)
    try:
        ins_offer = Offer.objects.get(fk_product=int_id)
        return render(request, 'view_product.html', {'product': ins_product, 'offer': ins_offer})
    except:
        return render(request, 'view_product.html', {'product': ins_product})


def logout(request):
    auth.logout(request)
    return redirect('login')