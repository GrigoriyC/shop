from django.shortcuts import render

from shop.models import Product


def get_product_list(request):
  products = Product.objects.all()

  return render(request, 'shop/product_list.html', context={'products': products})
