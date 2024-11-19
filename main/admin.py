from django.contrib import admin

from .models import Product  # Impor model Product

# Mendaftarkan model Product di Django Admin
admin.site.register(Product)