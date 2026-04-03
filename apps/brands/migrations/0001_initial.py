from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('name_ru', models.CharField(max_length=255, null=True, blank=True)),
                ('name_uz', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.TextField(blank=True)),
                ('description_ru', models.TextField(blank=True, null=True)),
                ('description_uz', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
                'ordering': ['name'],
            },
        ),
    ]
