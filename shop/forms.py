from django import forms


class ProductForm(forms.Form):
  title = forms.CharField(
    max_length=200,
    label="Наименование товара:",
    required=False,
    widget=forms.TextInput(attrs={
      'placeholder': "Наименование (максимальная длина 200 символов)"
    }) # Можно передавать другие атрибуты, например, "class": 'title-input'
  )

  text = forms.CharField(
    label="Описание товара:",
    widget=forms.Textarea(attrs={
      'row': 3
    })
  )

  price = forms.CharField(
  label="Цена товара:",
  #widget=forms.Textarea(attrs={
   # 'row': 1
  #})
)

  def clean_title(self):
    title = self.cleaned_data['title'].strip()

    if not title:
      raise forms.ValidationError("Наименование обязательно.")
    
    if len(title) < 5:
      raise forms.ValidationError("Наименование не должно быть короче 5 символов.")
    
    return title
  

  def clean_price(self):
    price = self.cleaned_data['price'].strip()

    if not price:
      raise forms.ValidationError("Цена товара обязательна.")
  
    #if len(price) < 5:
      #raise forms.ValidationError("Наименование не должно быть короче 5 символов.")
  
    return price
  