from django.db import models


# Create your models here.
class Cat1(models.Model):
    description = models.CharField(max_length=64, null=True)


class Curricula(models.Model):
    title = models.CharField(max_length=100, verbose_name='课程标题')
    # picture = models.ImageField
    desc = models.CharField(max_length=640, verbose_name='课程描述', null=True)
    coach = models.ForeignKey(to='account.Users', related_name='curriculum', on_delete=None, default=1)
    # start_time = models.DateTimeField(verbose_name='上课时间')
    duration = models.IntegerField(verbose_name='授课时长', null=True)
    status = models.IntegerField(verbose_name='课程状态', null=True)
    location = models.CharField(max_length=512, verbose_name='授课地点', null=True)
