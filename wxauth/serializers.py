
from dataclasses import fields
from rest_framework import serializers
from .models import TOTP


class TOTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = TOTP
        fields = [
            "id",
            "session",
            "isuser",
            "remark",
            "secret",
            "create_date",
        ]