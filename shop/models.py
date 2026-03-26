
from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="Назва")
    slug = models.SlugField(max_length=120,unique=True, db_index=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"



class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Опис")
    created_at = models.DateTimeField(auto_created=True, verbose_name="Дата публікації")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    slug = models.SlugField(max_length=220,unique=True, db_index=True, blank=True)
    image = models.ImageField(upload_to='shop/products')

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новина"
        verbose_name_plural = "Новини"


