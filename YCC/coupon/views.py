from django.shortcuts import render
from django.http import HttpResponse
from .models import Store, Coupon
import csv

def coupon_popup_view(request, store_id):
    store = Store.objects.get(id=store_id)
    coupon_code = request.GET.get('code')
    coupon_url = request.GET.get('url')
    return render(request, 'store/coupon-popup.html', {'store': store, 'coupon_code': coupon_code, 'coupon_url': coupon_url})


def import_csv(request):
    csv_file = request.FILES['csv_file']
    Coupon.import_csv(csv_file)  
    return HttpResponse("Import successful!")
