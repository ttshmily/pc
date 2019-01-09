from django.db import models
from account.models import Users


# Create your models here.
class Cat1(models.Model):
    pass


class SKU(models.Model):
    title = models.CharField(max_length=100, verbose_name='课程标题')
    picture = models.ImageField
    desc = models.CharField(max_length=640, verbose_name='课程描述')
    coach = models.ForeignKey(to=Users)
    start_time = models.DateTimeField(verbose_name='上课时间')
    duration = models.IntegerField(verbose_name='授课时长', max_length=60)
    status = models.IntegerField(verbose_name='课程状态', max_length=10)
    location = models.CharField(max_length=512, verbose_name='授课地点')
