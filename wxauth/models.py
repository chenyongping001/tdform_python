from django.db import models

# Create your models here.


class WXUser(models.Model):
    session = models.CharField(max_length=255)
    openid = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20,null=True,blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

# 合法的外协人员
class HfWxUser(models.Model):
    username = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    can_add = models.BooleanField(default=False)

# 保存TOTP信息
class TOTP(models.Model):
    session = models.CharField(max_length=255)
    isuser = models.CharField(max_length=255,null=True,blank=True)
    remark = models.CharField(max_length=255,null=True,blank=True)
    secret = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)

