from django.db.models import Q
from django.shortcuts import render

from .models import Category


def category_list(request):
    query = request.GET.get("q", "").strip()
    has_products = request.GET.get("has_products")

    categories = Category.objects.all()
    if query:
        categories = categories.filter(Q(name__icontains=query) | Q(description__icontains=query))

    # Annotate product count in Python to avoid MongoDB aggregation issues
    category_list_data = list(categories)
    for cat in category_list_data:
        cat.product_count = cat.products.count()

    if has_products == "1":
        category_list_data = [c for c in category_list_data if c.product_count > 0]

    context = {
        "categories": category_list_data,
        "query": query,
        "has_products": has_products,
    }
    return render(request, "categories.html", context)
