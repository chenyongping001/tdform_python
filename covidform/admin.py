from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.TempInto)
admin.site.register(models.TempintoFile)
admin.site.register(models.OvertimeInto)
admin.site.register(models.OvertimeIntoFile)
admin.site.register(models.Clrc)
admin.site.register(models.ClrcFile)
