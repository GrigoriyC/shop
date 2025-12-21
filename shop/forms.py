from django import forms

from shop.models import Product

class ProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = ['title', 'text', 'price']
    widgets = {
      'title': forms.TextInput(attrs={
        'placeholder': "наименование (максимальная длина 200 символов)"
      })
    }
    labels = {
      'title': 'Наименование товара:',
      'text': 'Описание товара:',
      'price': 'Цена'
    }

  def clean_title(self):
    title = self.cleaned_data['title'].strip()

    if not title:
      raise forms.ValidationError("Наименование обязательно.")
    
    if len(title) < 5:
      raise forms.ValidationError("Наименование не должно быть короче 5 символов.")
    
    return title
  

  def clean_price(self):
    price = self.cleaned_data['price']

    if not price:
      raise forms.ValidationError("Цена товара обязательна.")
  
    #if len(price) < 5:
      #raise forms.ValidationError("Наименование не должно быть короче 5 символов.")
  
    return price
  