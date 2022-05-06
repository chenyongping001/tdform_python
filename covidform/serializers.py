from .models import TempInto, TempintoFile, OvertimeInto, OvertimeIntoFile,Clrc,ClrcFile
from rest_framework import serializers


class TempintoFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempintoFile
        fields = ['file']

    def create(self, validated_data):
        tempinto_id = self.context['tempinto_id']
        return TempintoFile.objects.create(tempinto_id=tempinto_id, **validated_data)


class TempIntoSerializer(serializers.ModelSerializer):
    files = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = TempInto
        fields = ["id",
                  "weixinID",
                  "name",
                  "iccard",
                  "healthValue",
                  "daysValue",
                  "outProvinceValue",
                  "outCompany",
                  "project",
                  "reason",
                  "note",
                  "contact",
                  "contactPhone",
                  "createtime",
                  "last_update",
                  "status",
                  "files"]

# ------------------------------------------------------------

class OvertimeIntoFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = OvertimeIntoFile
        fields = ['file']

    def create(self, validated_data):
        overtimeinto_id = self.context['overtimeinto_id']
        return OvertimeIntoFile.objects.create(overtimeinto_id=overtimeinto_id, **validated_data)

class OvertimeIntoSerializer(serializers.ModelSerializer):
    files = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = OvertimeInto
        fields = ["id",
                  "weixinID",
                  "name",
                  "iccard",
                  "reason",
                  "note",
                  "gateValue",
                  "contact",
                  "contactPhone",
                  "createtime",
                  "last_update",
                  "status",
                  "files"]

# --------------------------------------------------------

class ClrcFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClrcFile
        fields = ['file']

    def create(self, validated_data):
        clrc_id = self.context['clrc_id']
        return ClrcFile.objects.create(clrc_id=clrc_id, **validated_data)


class ClrcSerializer(serializers.ModelSerializer):
    files = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Clrc
        fields = ["id",
                  "wx_session",
                  "gcmc",
                  "sgdw",
                  "jhjcksrq",
                  "jhjcjsrq",
                  "cx",
                  "cphm",
                  "tssgcl",
                  "jsy",
                  "sqly",
                  "dclxrxm",
                  "dclxrsj",
                  "create_time",
                  "last_update",
                  "status",
                  "files"]
