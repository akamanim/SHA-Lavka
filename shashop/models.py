from django.db import models
from django.utils.text import slugify
from account.models import User


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('-name',)

    name = models.CharField(max_length=100, verbose_name='Название категрии')
    slug = models.SlugField(unique=True, verbose_name='Название ссылки на категории', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return f'категория - {self.name}'


class Product(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('-name',)
    name = models.CharField(max_length=100, verbose_name='название продукта')
    description = models.TextField(verbose_name='описание товара')
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    slug = models.SlugField(unique=True,verbose_name='ссылка на товар', blank=True, null=True)
    activ = models.BooleanField(default=False, verbose_name='в наличии или нет')
    created = models.DateField(auto_now_add=True, verbose_name='дата добавления')
    count_product = models.PositiveIntegerField(default=0, verbose_name= 'кол-во товара на складе')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Order #{self.order.id})"
