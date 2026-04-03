import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(
                    blank=True,
                    null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    related_name='order_requests',
                    to='products.product',
                )),
                ('product_name', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=50)),
                ('message', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Order Request',
                'verbose_name_plural': 'Order Requests',
                'ordering': ['-created_at'],
            },
        ),
    ]
