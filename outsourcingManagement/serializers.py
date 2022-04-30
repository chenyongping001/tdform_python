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

    class Meta:
        model = Workbook
        fields = ["id",
                  "wx_session",
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