from django.db import models


# Create your models here.
class Users(models.Model):
    user_id = models.CharField(max_length=20, verbose_name='用户ID')
    login_type = models.CharField(max_length=20, verbose_name='登录类型')
    mobile = models.CharField(max_length=11, verbose_name='手机号')
    email = models.EmailField(verbose_name='邮箱')
    open_id = models.CharField(max_length=20, verbose_name='微信ID')
    password = models.CharField(max_length=100, verbose_name='登录密码')

    nickname = models.CharField(max_length=20, verbose_name='用户昵称')
    avatar = models.ImageField(upload_to='avatar', verbose_name='头像', null=True, default='xxx')
    age = models.IntegerField(verbose_name='年龄')
    gender = models.IntegerField(verbose_name='性别')
    create_date = models.DateField(verbose_name='创建日期', null=False)
    last_login_date = models.DateField(verbose_name='最后登录日期', null=False)
    last_login_ip = models.IPAddressField(verbose_name='最后登录IP', null=True)

