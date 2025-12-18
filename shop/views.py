from django.shortcuts import render, get_object_or_404, redirect

from shop.models import Product


def get_product_list(request):
  products = Product.objects.all()

  return render(request, 'shop/product_list.html', context={'products': products})


def get_product_detail(request, product_id):
  return render(request, 'shop/product_detail.html', {"product": get_object_or_404(Product, id=product_id)})


def create_product(request):
  if request.method == "GET":
    return render(request, 'shop/product_add.html')
  
  if request.method == "POST":
    product = Product.objects.create(title=request.POST.get('title'), text=request.POST.get('text'), price=request.POST.get('price'))

    return redirect('product_detail', product_id=product.id)
