from typing import Any
from django.conf import settings
from django.db import models
from rest_framework.response import Response

# Create your models here.


class TempInto(models.Model):
    HEALTH_CHOICE = [
        (1, '绿码'),
        (0, '非绿码')
    ]
    DAYS_CHOICE = [
        (1, '1天'),
        (2, '2天'),
        (3, '3天'),
    ]
    OUT_PROVINCE_CHOICE = [
        (0, '未出过省'),
        (1, '出过省'),
    ]
    STATUS_CHOICE = [
        (0, '待处理'),
        (1, '找不到联系人'),
        (2, '已生成申请单'),
        (3, '审批中'),
        (4, '通过'),
        (5, '拒绝'),
        (6, '已删除'),
    ]

    weixinID = models.CharField(max_length=255)
    name = models.CharField(max_length=10)
    iccard = models.CharField(max_length=18)
    healthValue = models.PositiveSmallIntegerField(
        choices=HEALTH_CHOICE, default=1)
    daysValue = models.PositiveSmallIntegerField(
        choices=DAYS_CHOICE, default=1)
    outProvinceValue = models.PositiveSmallIntegerField(
        choices=OUT_PROVINCE_CHOICE, default=0)
    outCompany = models.CharField(max_length=255)
    project = models.CharField(max_length=255, null=True, blank=True)
    reason = models.TextField()
    note = models.TextField(null=True, blank=True)
    contact = models.CharField(max_length=10)
    contactPhone = models.CharField(max_length=11)
    createtime = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICE, default=0)


class TempintoFile(models.Model):
    # file = models.ImageField(upload_to='covid19/')
    file = models.FileField(upload_to='covid19/')
    tempinto = models.ForeignKey(
        TempInto, related_name='files', on_delete=models.CASCADE)

    def __str__(self):
        return settings.MEDIA_URL+str(self.file)


class OvertimeInto(models.Model):
    GATE_CHOICE = [
        (1, '一号门'),
        (2, '厂前区'),
    ]
    STATUS_CHOICE = [
        (0, '待处理'),
        (1, '无此持卡人'),
        (2, '找不到联系人'),
        (3, '已生成申请单'),
        (4, '审批中'),
        (5, '通过'),
        (6, '已删除'),
        (7, '施工证已过期'),
    ]
    weixinID = models.CharField(max_length=255)
    name = models.CharField(max_length=10)
    iccard = models.CharField(max_length=18)
    reason = models.TextField()
    note = models.TextField(null=True, blank=True)
    gateValue = models.PositiveSmallIntegerField(
        choices=GATE_CHOICE, default=1)
    contact = models.CharField(max_length=10)
    contactPhone = models.CharField(max_length=11)
    createtime = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICE, default=0)


class OvertimeIntoFile(models.Model):
    # OT代表超时overtime
    file = models.FileField(upload_to='covid19_OT/')
    overtimeinto = models.ForeignKey(
        OvertimeInto, related_name='files', on_delete=models.CASCADE)

    def __str__(self):
        return settings.MEDIA_URL+str(self.file)



# 临时车辆入厂
class Clrc(models.Model):
    TSSGCL_CHOICE = [
        (0, '否'),
        (1, '是'),
    ]
    STATUS_CHOICE = [
        (0, '待处理'),
        (1, '找不到联系人'),
        (2, '已生成申请单'),
        (3, '审批中'),
        (4, '通过'),
        (5, '删除'),
    ]
    wx_session = models.CharField(max_length=255)
    gcmc = models.CharField(max_length=255)
    sgdw = models.CharField(max_length=255)
    jhjcksrq = models.DateField()
    jhjcjsrq = models.DateField()
    cx = models.CharField(max_length=20)
    cphm = models.CharField(max_length=10)
    tssgcl = models.PositiveSmallIntegerField(
        choices=TSSGCL_CHOICE, default=0)
    jsy = models.CharField(max_length=10,blank=True,null=True)
    sqly = models.TextField()
    dclxrxm = models.CharField(max_length=10)
    dclxrsj = models.CharField(max_length=11)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICE, default=0)


class ClrcFile(models.Model):
    file = models.FileField(upload_to='clrc/')
    clrc = models.ForeignKey(
        Clrc, related_name='files', on_delete=models.CASCADE)

    def __str__(self):
        return settings.MEDIA_URL+str(self.file)
