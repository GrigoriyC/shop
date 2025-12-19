from django.shortcuts import render, get_object_or_404, redirect

from shop.models import Product


def get_product_list(request):
  products = Product.objects.all()

  return render(request, 'shop/product_list.html', context={'products': products})


def get_product_detail(request, product_id):
  return render(request, 'shop/product_detail.html', {"product": get_object_or_404(Product, id=product_id)})


def create_product(request):
  if request.method == "POST":
    #product = Product.objects.create(title=request.POST.get('title'), text=request.POST.get('text'), price=request.POST.get('price'))
    title = request.POST.get('title').strip()
    text = request.POST.get('text').strip()
    price = request.POST.get('price').strip()

    errors = {}

    if not title:
      errors['title'] = 'Наименование товара обязательно.'
    if not text:
      errors['text'] = 'Описание товара обязательно нужно указать.'
    if not price:
      errors['price'] = 'Цену товара обязательно нужно указать.'    

    if not errors:
      product = Product.objects.create(title=title, text=text, price=price)

      return redirect('product_detail', product_id=product.id)
    else:
      context = {
        'errors': errors,
        'title': title,
        'text': text,
        'price': price
      }

      return render(request, 'shop/product_add.html', context)
    
  return render(request, 'shop/product_add.html')
