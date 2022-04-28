from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.WXUser)
admin.site.register(models.HfWxUser)
