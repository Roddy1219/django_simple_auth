from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
'''
    使用直接AbstractUser的方式建立用户表，这样只作扩展属性比较简单
'''
class User(AbstractUser):
    mobile = models.CharField(max_length=20, verbose_name="手机号")
    SEX_TYPE = (
        ('0', '男'),
        ('1', '女'),
    )
    sex = models.CharField(max_length=1, choices=SEX_TYPE,default='0')

    image = models.ImageField(default='', upload_to='images/%Y/%m', verbose_name='头像', max_length=100)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = verbose_name


