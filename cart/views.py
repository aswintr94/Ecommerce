from django.shortcuts import render, redirect
from .models import Cart
from products.models import Product
from offer.models import Offer
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import F

# Create your views here.
def add_to_cart(request, pro_id):
    Cart.objects.create(fk_product=Product.objects.get(id=pro_id), fk_offer=Offer.objects.get(fk_product=pro_id), fk_user=User.objects.get(id=request.user.id), int_status=0)
    messages.success(request, 'Item added to cart')
    return redirect(view_cart)

def view_cart(request):
    # import pdb; pdb.set_trace()
    ins_cart = Cart.objects.filter(fk_user=request.user.id, int_status=0)
    values = ins_cart.annotate(intPrice=F('fk_offer__int_offer_price')).values('intPrice')
    int_total = 0
    discount_amount = 0
    for i in values:
        int_total += i['intPrice']

    if int_total > 20000:
        discount_amount = int_total * 80//100
    else:
        pass

    amount = {}
    amount['int_total'] = int_total
    amount['final_amount'] = discount_amount
    if discount_amount > 0:
        amount['discount'] = 20

    return render(request, 'view_cart.html', {'cart': ins_cart, 'amount': amount})

def remove_item(request, item_id):
    ins_cart = Cart.objects.get(id=item_id)
    ins_cart.delete()
    return redirect(view_cart)