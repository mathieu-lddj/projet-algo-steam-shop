from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product
# Create your views here.
def index(request):
    products = Product.objects.all()
    return HttpResponse(render(request, 'store/index.html', context={"products": products}))