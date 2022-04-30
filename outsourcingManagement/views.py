from django.shortcuts import render

# Create your views here.
import json
import os
from pathlib import Path
from django.forms.models import model_to_dict
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime, timedelta
from .models import Workbook,WorkbookFile
from .serializers import WorkbookSerializer,WorkbookFileSerializer
from django.conf import settings

class WorkbookViewSet(viewsets.ModelViewSet):
    serializer_class = WorkbookSerializer

    def get_queryset(self):
        queryset = Workbook.objects.prefetch_related('files').all()
        wx_session = self.request.query_params.get('wx_session')
        if(wx_session):
            queryset = queryset.filter(wx_session=wx_session)
        return queryset.order_by("-create_time")


class WorkbookFileViewSet(viewsets.ModelViewSet):
    serializer_class = WorkbookFileSerializer

    def get_queryset(self):
        return WorkbookFile.objects.filter(workbook_id=self.kwargs['workbook_pk'])

    def get_serializer_context(self):
        return {'workbook_id': self.kwargs['workbook_pk']}