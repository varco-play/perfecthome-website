import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brands', '0001_initial'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_ru', models.CharField(max_length=100, null=True, blank=True)),
                ('name_uz', models.CharField(max_length=100, null=True, blank=True)),
                ('slug', models.SlugField(max_length=120, unique=True)),
            ],
            options={
                'verbose_name': 'Product Tag',
                'verbose_name_plural': 'Product Tags',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('name_ru', models.CharField(max_length=255, null=True, blank=True)),
                ('name_uz', models.CharField(max_length=255, null=True, blank=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('description_ru', models.TextField(null=True, blank=True)),
                ('description_uz', models.TextField(null=True, blank=True)),
                ('category', models.ForeignKey(
                    blank=True,
                    null=True,
                    on_delete=django.db.models.deletion.DO_NOTHING,
                    related_name='products',
                    to='categories.category',
                )),
                ('brand', models.ForeignKey(
                    blank=True,
                    null=True,
                    on_delete=django.db.models.deletion.DO_NOTHING,
                    related_name='products',
                    to='brands.brand',
                )),
                ('country_of_origin', models.CharField(max_length=120)),
                ('country_of_origin_ru', models.CharField(max_length=120, null=True, blank=True)),
                ('country_of_origin_uz', models.CharField(max_length=120, null=True, blank=True)),
                ('article_number', models.CharField(max_length=120)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('tags', models.ManyToManyField(blank=True, related_name='products', to='products.producttag')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/images/')),
                ('alt_text', models.CharField(blank=True, max_length=255)),
                ('alt_text_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('alt_text_uz', models.CharField(blank=True, max_length=255, null=True)),
                ('product', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='images',
                    to='products.product',
                )),
            ],
            options={
                'verbose_name': 'Product Image',
                'verbose_name_plural': 'Product Images',
                'ordering': ['id'],
            },
        ),
    ]
