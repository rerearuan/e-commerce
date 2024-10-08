import datetime
from django.views.decorators.csrf import csrf_protect
from django.utils.html import strip_tags
from django.http import HttpResponseRedirect
from decimal import Decimal
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.shortcuts import render, redirect
from main.forms import ProductEntryForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

@login_required(login_url='/login')
def show_main(request):

    context = {
        'name': request.user.username,
        'last_login': request.COOKIES.get('last_login'),
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
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user=request.user)
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
        messages.error(request, "Invalid username or password. Please try again.")
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
    product = Product.objects.get(pk=id)
    form = ProductEntryForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        product.name = strip_tags(form.cleaned_data['name'])
        product.description = strip_tags(form.cleaned_data['description'])
        product.category = strip_tags(form.cleaned_data['category'])
        product.review = strip_tags(form.cleaned_data['review'])
        product.price = form.cleaned_data['price']  
        product.stock = form.cleaned_data['stock']  
        product.rating = form.cleaned_data['rating']  

        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = Product.objects.get(pk=id)  #
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
        name = strip_tags(request.POST.get("name"))
        description = strip_tags(request.POST.get("description"))
        category = strip_tags(request.POST.get("category"))
        review = strip_tags(request.POST.get("review"))
        price = Decimal(request.POST.get("price", 0))
        stock = int(request.POST.get("stock", 0))
        rating = float(request.POST.get("rating", 0))

        user = request.user

        new_product = Product(
            name=name,
            price=price,
            description=description,
            stock=stock,
            category=category,
            rating=rating,
            review=review,
            user=user
        )
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    