from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Offer
from products.models import Product

# Create your views here.
def add_offer(request):
    if request.method == 'POST':
        # import pdb; pdb.set_trace()
        int_offer_id = int(request.POST.get('intOfferId'))
        int_offer_price = int(request.POST.get('strOfferPrice'))
        int_product_id = Offer.objects.get(id=int_offer_id).fk_product.id
        int_pro_price = Product.objects.get(id=int_product_id).int_price

        int_discount = int(100-(int_offer_price/int_pro_price)*100)
        Offer.objects.filter(id=int_offer_id).update(int_offer_price=int_offer_price, int_offer_percent=int_discount)
        return redirect(add_offer)
    else:
        ins_offer = Offer.objects.all()
        return render(request, 'add_offer.html', {'products': ins_offer})