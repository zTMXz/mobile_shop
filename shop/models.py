import datetime

from django.db import models
from users.models import User
from django.urls import reverse



class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=60, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])


class PhoneDetails(models.Model):
    model = models.CharField(max_length=100, default='')
    display = models.TextField()
    processor = models.TextField()
    size_and_weight = models.TextField()
    camera = models.TextField()
    video = models.TextField()
    front_cam = models.TextField()
    mobile_cnct = models.TextField()
    os = models.CharField(max_length=25, default='')

    class Meta:
        ordering = ('model',)
        verbose_name = 'Детали телефона'
        verbose_name_plural = 'Детали телефонов'

    def __str__(self):
        return self.model


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(default='slug', max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(default=datetime.datetime.now())
    updated = models.DateTimeField(default=datetime.datetime.now())
    memory = models.CharField(max_length=10, default='0GB')
    ram = models.CharField(max_length=10, default='0GB')
    ph_color_hex = models.CharField(max_length=50, default='')
    ph_color_name = models.CharField(max_length=50, default='')
    details = models.ForeignKey(PhoneDetails, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])


class PhoneConfiguration(models.Model):
    phone_id = models.ForeignKey(Product, related_name='configuration', on_delete=models.CASCADE)
    phone_configurations = models.ManyToManyField(Product, related_name='Configurations')

    class Meta:
        verbose_name = 'Конфигурация'
        verbose_name_plural = 'Конфигурации телефонов'

    def __str__(self):
        return self.phone_id.name


class PhoneColors(models.Model):
    phone_id = models.ForeignKey(Product, related_name='color', on_delete=models.CASCADE)
    phone_colors = models.ManyToManyField(Product, related_name='Colors')

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета телефонов'

    def __str__(self):
        return self.phone_id.name
