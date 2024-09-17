from django.shortcuts import render, redirect
from main.forms import ProductEntryForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers


def show_main(request):
    product_entries = Product.objects.all()

    products = [
        {
            'name': 'Bamboo Chair',
            'price': 99.99,
            'description': 'A comfortable bamboo chair.',
            'stock': 10,
            'category': 'Furniture',
            'rating': 4.5,
            'date_added': '2024-09-01',
            'review': 'Very comfortable and eco-friendly!'
        },
        {
            'name': 'Bamboo Tshirt',
            'price': 29.99,
            'description': 'A stylish bamboo t-shirt.',
            'stock': 50,
            'category': 'Fashion',
            'rating': 4.2,
            'date_added': '2024-08-15',
            'review': 'Soft and breathable material!'
        },
        {
            'name': 'Bamboo Decor ',
            'price': 15.99,
            'description': 'Elegant bamboo decor for your home.',
            'stock': 20,
            'category': 'Home Decor',
            'rating': 4.8,
            'date_added': '2024-07-10',
            'review': 'Adds a touch of nature to any room!'
        }

    
    ]

    context = {
        'products': products,
        'product_entries' :  product_entries

    }

    return render(request, "main.html", context)

def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "create_product_entry.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")