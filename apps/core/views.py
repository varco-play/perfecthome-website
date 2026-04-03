from django.conf import settings
from django.shortcuts import render


def home(request):
    from apps.blog.models import BlogPost
    from apps.brands.models import Brand
    from apps.categories.models import Category
    from apps.products.models import Product

    featured_categories = Category.objects.all()[:8]
    featured_products = Product.objects.with_related().order_by("-created_at")[:8]
    brands = Brand.objects.all()[:12]
    latest_posts = BlogPost.objects.order_by("-created_at")[:3]

    # Attach product counts in Python
    for cat in featured_categories:
        cat.product_count = cat.products.count()
    for brand in brands:
        brand.product_count = brand.products.count()

    context = {
        "featured_categories": featured_categories,
        "featured_products": featured_products,
        "brands": brands,
        "latest_posts": latest_posts,
    }
    return render(request, "home.html", context)


def about(request):
    return render(request, "about.html")


def contact(request):
    context = {
        "address": settings.CONTACT_ADDRESS,
        "phone": settings.CONTACT_PHONE,
        "email": settings.CONTACT_EMAIL,
        "map_url": settings.CONTACT_MAP_EMBED_URL,
    }
    return render(request, "contact.html", context)
