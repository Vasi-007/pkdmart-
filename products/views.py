from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductForm
from .models import Category, Product


class UserLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return '/dashboard/'


@login_required
def dashboard(request):
    total_products = Product.objects.count()

    active_products = Product.objects.filter(status=True).count()

    inactive_products = Product.objects.filter(status=False).count()

    low_stock_products = Product.objects.filter(stock__lte=5).count()

    context = {
        'total_products': total_products,
        'active_products': active_products,
        'inactive_products': inactive_products,
        'low_stock_products': low_stock_products,
    }

    return render(request,'dashboard.html',context)


@login_required
def product_list(request):
    products = Product.objects.select_related('category').all()

    search = request.GET.get('search', '').strip()
    category = request.GET.get('category', '')
    status = request.GET.get('status', '')

    if search:
        products = products.filter(name__icontains=search)

    if category:
      products = products.filter(category_id=category)

    if status == 'active':
        products = products.filter(status=True)

    elif status == 'inactive':
        products = products.filter(status=False)

    categories = Category.objects.all()
    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'categories': categories,
        'search': search,
        'selected_category': category,
        'selected_status': status,
    }

    return render(request,'productlist.html',context)


@login_required
def product_create(request):

    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()

            return redirect('products:product_list')

    else:
        form = ProductForm()

    context = {
        'form': form,
        'page_title': 'Add Product',
        'button_text': 'Add Product',
    }

    return render(request,'productform.html',context)


@login_required
def product_update(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk
    )

    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES,instance=product)

        if form.is_valid():
            form.save()

            return redirect('products:product_list')

    else:
        form = ProductForm(instance=product)

    context = {
        'form': form,
        'product': product,
        'page_title': 'Edit Product',
        'button_text': 'Update Product',
    }

    return render(request,'productform.html',context)


@login_required
def product_delete(request, pk):

    product = get_object_or_404(Product,pk=pk)

    if request.method == 'POST':
        product.delete()

    return redirect('products:product_list')