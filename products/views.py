from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404

# Create your views here.
def index (request):
  products = Product.objects.all().order_by('name')
  context = {'products': products}
  return render(request, 'products/index.html', context)

def show (request, product_id):
  p = get_object_or_404(Product, pk=product_id)
  context = { 'product':p }
  return render(request, 'products/show.html', context)

