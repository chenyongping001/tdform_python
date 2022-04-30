from django.db import models
from django.conf import settings

# Create your models here.
class Workbook(models.Model):
    wx_session = models.CharField(max_length=255)
    rq = models.DateField()
    yh = models.CharField(max_length=10)
    sbhxt = models.CharField(max_length=255)
    tzr = models.CharField(max_length=10)
    gzxxhyy = models.TextField()
    clkssj = models.TimeField()
    clgcsm = models.TextField()
    cljssj = models.TimeField()
    jqfx = models.TextField(blank=True,null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

class WorkbookFile(models.Model):
    file = models.FileField(upload_to='workbook/')
    workbook = models.ForeignKey(
        Workbook, related_name='files', on_delete=models.CASCADE)

    def __str__(self):
        return settings.MEDIA_URL+str(self.file)