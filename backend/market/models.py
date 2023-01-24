from django.db import models
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.forms.models import model_to_dict
from datetime import datetime

class Type(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название типа товара')
    description = models.TextField(verbose_name='Описание типа товара', blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название товара')
    price = models.FloatField(verbose_name='Цена товара', default=0)
    CURRENCY_CHOICES = (
        ("rub", "Рубль"),
        ("usd", "Доллар"),
        ("eur", "Евро")
    )
    currency = models.CharField(max_length=6, verbose_name='Валюта', choices=CURRENCY_CHOICES, default="rub")
    in_stock = models.IntegerField(verbose_name='Остаток на складе', default=0)
    code = models.CharField(max_length=20, verbose_name='Штрихкод', blank=True)
    image = models.ImageField(verbose_name='Картинка товара', blank=True)
    date_update = models.DateField( verbose_name='Обновлён')
    type_product = models.ForeignKey(Type, on_delete = models.SET_NULL, verbose_name="Тип товара", related_name='product_type', null=True)
    manufacturer = models.CharField(max_length=70, verbose_name='Поставщик')

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='Имя клиента')
    adress = models.CharField(max_length=100, verbose_name='Адрес клиента')
    cart = models.ManyToManyField(Product)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Product)
def product_handler_create_update(sender, instance, created, **kwargs):
    print('save product signal create')
    channel_layer = get_channel_layer()
    obh = {
        "id": instance.id,
        "name": instance.name,
        "price": instance.price,
        "currency": instance.currency,
        "in_stock": instance.in_stock,
        "code": instance.code,
        "image": instance.image.url,
        "date_update": str(datetime.now()),
        "type_product": model_to_dict(instance.type_product),
        "manufacturer": instance.manufacturer
    }
    async_to_sync(channel_layer.group_send)(
        'products',{
            'type': 'product.save',
            'value': obh
        }
    )

@receiver(post_delete, sender=Product)
def product_handler_delete(sender, instance, *args, **kwargs):
    print('delete product signal create')
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'products',{
            'type': 'product.delete',
            'value': instance.id
        }
    )