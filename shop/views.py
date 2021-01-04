from django.shortcuts import render
from .models import Product
from math import ceil
from django.http import HttpResponse

def index(request):
    # products = Product.objects.all()
    # print(products)
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides), nSlides])
    # allProds = [[products, range(1, nSlides ), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    context = {'allProds':allProds}

    return render(request, 'shop/index.html', context)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request, myid):
    #fetch product using id 
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, 'shop/prodView.html', {'product':product[0]})

def checkout(request):
    return render(request, 'shop/checkout.html')



