from django.db.models import Q
from django.shortcuts import render

from .models import Brand


SORT_MAP = {
    "name": "name",
    "-name": "-name",
}


def brand_list(request):
    query = request.GET.get("q", "").strip()
    sort = request.GET.get("sort", "name")

    brands = Brand.objects.all()
    if query:
        brands = brands.filter(Q(name__icontains=query) | Q(description__icontains=query))

    ordering = SORT_MAP.get(sort, "name")
    brands = brands.order_by(ordering)

    # Annotate product count in Python to avoid MongoDB aggregation issues
    brand_list_data = list(brands)
    for brand in brand_list_data:
        brand.product_count = brand.products.count()

    context = {
        "brands": brand_list_data,
        "featured_brands": brand_list_data[:2],
        "query": query,
        "sort": sort,
    }
    return render(request, "brands.html", context)
