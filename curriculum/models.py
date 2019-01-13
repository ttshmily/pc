from django.db import models


# Create your models here.
class Cat1(models.Model):
    category_name = models.CharField(max_length=10, null=False, verbose_name='课程类型', default='输入名称')
    description = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = '课程类型'
        verbose_name_plural = verbose_name


class Curricula(models.Model):
    title = models.CharField(max_length=100, verbose_name='课程标题', default='输入课程标题')
    picture = models.ImageField(upload_to='curricula', verbose_name='展示图片', default='show.jpg')
    desc = models.CharField(max_length=640, verbose_name='课程描述', null=True)
    coach = models.ForeignKey(to='account.Users', related_name='curriculum', verbose_name='教练', on_delete=None, default=1)
    category = models.ForeignKey(to='Cat1', verbose_name='课程类型', null=False, default=1, on_delete=None)
    start_time = models.DateTimeField(verbose_name='上课时间', null=True)
    duration = models.IntegerField(verbose_name='授课时长', null=True)
    status = models.IntegerField(verbose_name='课程状态', null=True)
    location = models.CharField(max_length=512, verbose_name='授课地点', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '课程表'
        verbose_name_plural = verbose_name

