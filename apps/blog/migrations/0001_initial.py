from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_ru', models.CharField(max_length=255, null=True, blank=True)),
                ('title_uz', models.CharField(max_length=255, null=True, blank=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('content', models.TextField()),
                ('content_ru', models.TextField(null=True, blank=True)),
                ('content_uz', models.TextField(null=True, blank=True)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='blog/covers/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Blog Post',
                'verbose_name_plural': 'Blog Posts',
                'ordering': ['-created_at'],
            },
        ),
    ]
