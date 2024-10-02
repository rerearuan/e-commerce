import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from main.forms import ProductEntryForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

@login_required(login_url='/login')
def show_main(request):
    product_entries = Product.objects.filter(user=request.user)

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
    ]

    context = {
        'name': request.user.username,
        'products': products,
        'product_entries' :  product_entries,
        'last_login': request.COOKIES['last_login']

    }

    return render(request, "main.html", context)

def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        Product_Entry = form.save(commit=False)
        Product_Entry.user = request.user
        Product_Entry.save()
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

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = Product.objects.get(pk = id)
    form = ProductEntryForm(request.POST or None, instance= product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = Product.objects.get(pk=id)  # Use Product instead of ProductEntryForm
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
