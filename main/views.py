from django.shortcuts import render

def show_main(request):
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
        'products': products
    }

    return render(request, "main.html", context)
