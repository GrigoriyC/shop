from django.shortcuts import render, get_object_or_404, redirect

from shop.models import Product
from shop.forms import ProductForm


def get_product_list(request):
  products = Product.objects.all()

  return render(request, 'shop/product_list.html', context={'products': products})


def get_product_detail(request, product_id):
  return render(request, 'shop/product_detail.html', {"product": get_object_or_404(Product, id=product_id)})


def create_product(request):
  if request.method == "POST":
    #product = Product.objects.create(title=request.POST.get('title'), text=request.POST.get('text'), price=request.POST.get('price'))
    form = ProductForm(request.POST)    

    if form.is_valid():
      product = Product.objects.create(
        title=form.cleaned_data['title'],
        text=form.cleaned_data['text'],
        price=form.cleaned_data['price']
      )    

      return redirect('product_detail', product_id=product.id)
    else:
      return render(request, 'shop/product_add.html', {"form": form})
    
  # GET
  form = ProductForm()
  
  return render(request, 'shop/product_add.html', {"form": form})
