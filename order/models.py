from django.db import models


# Create your models here.
class Orders(models.Model):
    order_id = models.AutoField(max_length=20, unique=True, verbose_name='订单ID', primary_key=True)
    product = models.CharField(max_length=20, verbose_name='商品ID')
