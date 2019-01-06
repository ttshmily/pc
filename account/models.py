from django.db import models
import hashlib


# Create your models here.
class Users(models.Model):
    user_id = models.AutoField(max_length=20, unique=True, verbose_name='用户ID', primary_key=True)

    login_type_choice = ((1, 'MOBILE'), (2, 'EMAIL'), (3, 'WX'))
    login_type = models.CharField(choices=login_type_choice, max_length=1, verbose_name='登录类型')
    mobile = models.CharField(max_length=11, verbose_name='手机')
    email = models.EmailField(verbose_name='邮箱')
    open_id = models.CharField(max_length=20, verbose_name='微信ID')
    password = models.CharField(max_length=100, verbose_name='登录密码')

    nickname = models.CharField(max_length=20, verbose_name='用户昵称')
    avatar = models.ImageField(upload_to='avatar', verbose_name='头像', null=True, default='xxx')
    age = models.IntegerField(verbose_name='年龄', null=True)
    gender = models.IntegerField(verbose_name='性别', null=True)
    create_date = models.TimeField(verbose_name='创建日期', null=False)
    last_login_date = models.TimeField(verbose_name='最后登录日期', null=False)
    last_login_ip = models.GenericIPAddressField(verbose_name='最后登录IP', null=True)

    # def save(self, *args, **kwargs):
    #     if self.user_id is None:
    #         self.password = hashlib.sha1(bytes(self.password, encoding='utf-8')).hexdigest()
    #     super(Users, self).save(*args, **kwargs)


class Tokens(models.Model):
    user = models.ForeignKey(to='Users', on_delete=models.DO_NOTHING)
    token = models.CharField(max_length=64)
    expire_to = models.TimeField(null=True)

