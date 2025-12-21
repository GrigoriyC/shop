from django.shortcuts import render, get_object_or_404, redirect

from shop.models import Product
from shop.forms import ProductForm


def get_product_list(request):
  products = Product.objects.all()

  return render(request, 'shop/product_list.html', context={'products': products})


def get_product_detail(request, product_id):
  return render(request, 'shop/product_detail.html', {"product": get_object_or_404(Product, id=product_id)})


def create_product(request):
  form = ProductForm(request.POST or None)

  if request.method == "POST":
    #product = Product.objects.create(title=request.POST.get('title'), text=request.POST.get('text'), price=request.POST.get('price'))
    if form.is_valid():
      product = form.save()     

      return redirect('product_detail', product_id=product.id)
    # Если форма невалидна, продолжим к render ниже  
  
  return render(request, 'shop/product_add.html', {"form": form})


def update_product(request, product_id):
  product = get_object_or_404(Product, id=product_id)

  if request.method == "POST":
    form = ProductForm(request.POST, instance=product)

    if form.is_valid():
      form.save()

      return redirect("product_detail", product_id=product.id)
    else:
      return render(request, 'shop/product_update.html', context={"form": form})

  form = ProductForm(instance=product)

  return render(request, 'shop/product_update.html', context={"form": form})
