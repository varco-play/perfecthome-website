# Intentionally empty — superseded by clean 0001_initial migration.
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('brands', '0003_brand_description_ru_brand_description_uz_and_more'),
        ('categories', '0004_category_description_ru_category_description_uz_and_more'),
        ('products', '0002_alter_product_slug_alter_producttag_slug'),
    ]
    operations = []
