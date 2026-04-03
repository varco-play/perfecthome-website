from django.forms import ModelForm
from apps.products.models import Product
from apps.categories.models import Category
from apps.brands.models import Brand
from apps.blog.models import BlogPost


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            "name", "slug", "description", "category", "brand",
            "country_of_origin", "article_number", "price", "tags",
        ]


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name", "slug", "image", "description"]


class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = ["name", "description"]


class BlogForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "slug", "content", "cover_image"]
