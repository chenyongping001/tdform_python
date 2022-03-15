from django.db import models

# Create your models here.


class WXUser(models.Model):
    session = models.CharField(max_length=255)
    openid = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)
