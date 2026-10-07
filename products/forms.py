from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            'name',
            'sku',
            'category',
            'price',
            'stock',
            'image',
            'description',
            'status',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control','placeholder': 'Enter product name'
            }),

            'sku': forms.TextInput(attrs={
                'class': 'form-control','placeholder': 'Enter SKU'
            }),

            'category': forms.Select(attrs={
                'class': 'form-select'
            }),

            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter price',
                'step': '0.01',
                'min': '0.01'
            }),

            'stock': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter stock quantity',
                'min': '0'
            }),

            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter product description'
            }),

            'status': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if not name or not name.strip():
            raise forms.ValidationError(
                'Product name is required.'
            )

        return name.strip()

    def clean_sku(self):
        sku = self.cleaned_data.get('sku')

        if not sku or not sku.strip():
            raise forms.ValidationError('SKU is required.')

        sku = sku.strip()

        existing_product = Product.objects.filter(sku__iexact=sku).exclude(
            pk=self.instance.pk
        ).exists()

        if existing_product:
            raise forms.ValidationError('A product with this SKU already exists.')

        return sku

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price is None or price <= 0:
            raise forms.ValidationError('Price must be greater than 0.')

        return price

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')

        if stock is None or stock < 0:
            raise forms.ValidationError('Stock cannot be negative.')

        return stock