from django.db import models


# Create your models here.
class BookInformation(models.Model):
    title = models.CharField(max_length=20, verbose_name='名称')
    pub_date = models.DateField(verbose_name='发布日期', null=True)
    read_count = models.IntegerField(default=1, verbose_name='阅读量')
    comment_count = models.IntegerField(default=0, verbose_name='评论量')
    book_cover = models.ImageField(upload_to='book_cover', verbose_name='封面', null=True)
