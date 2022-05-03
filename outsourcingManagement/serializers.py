from wxauth.models import HfWxUser, WXUser
from .models import Workbook,WorkbookFile
from rest_framework import serializers


class WorkbookFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkbookFile
        fields = ['file']

    def create(self, validated_data):
        workbook_id = self.context['workbook_id']
        return WorkbookFile.objects.create(workbook_id=workbook_id, **validated_data)


class WorkbookSerializer(serializers.ModelSerializer):
    files = serializers.StringRelatedField(many=True, read_only=True)
    # wx_username = serializers.SerializerMethodField(method_name="get_wxname")
    # def get_wxname(self,workbook:Workbook):
    #     phone_number = WXUser.objects.filter(session=workbook.wx_session).first().phone_number
    #     if(phone_number):
    #         return HfWxUser.objects.filter(phone_number=phone_number).first().username
    #     return None

    class Meta:
        model = Workbook
        fields = ["id",
                  "wx_session",
                  "wx_username", # 外协人员名字
                  "rq",
                  "yh",
                  "sbhxt",
                  "tzr",
                  "gzxxhyy",
                  "clkssj",
                  "clgcsm",
                  "cljssj",
                  "jqfx",
                  "create_time",
                  "update_time",
                  "files"]