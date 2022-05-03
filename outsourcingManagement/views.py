import math
from mmap import PAGESIZE
from django.http import JsonResponse
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
from django.db.models import Q

class WorkbookViewSet(viewsets.ModelViewSet):
    serializer_class = WorkbookSerializer

    def get_queryset(self):
        queryset = Workbook.objects.prefetch_related('files').all().order_by("-create_time")
        wx_session = self.request.query_params.get('wx_session')
        pagesize = self.request.query_params.get('pagesize')
        page = self.request.query_params.get('page')
        search = self.request.query_params.get('search')
        if(search):
            queryset = queryset.filter(Q(yh__icontains=search) | Q(tzr__icontains=search) | Q(wx_username__icontains=search) | Q(sbhxt__icontains=search) | Q(gzxxhyy__icontains=search) | Q(clgcsm__icontains=search))
        if(wx_session):
            queryset = queryset.filter(wx_session=wx_session)
        if(page and page.isnumeric()):
            if(pagesize and pagesize.isnumeric()):
                int_page = int(page)
                int_pagesize = int(pagesize)
                max_page = math.ceil(queryset.count()/int_pagesize)
                if(int_page>0 and int_page<=max_page):
                    start = (int_page -1)*int_pagesize
                    end = int_page * int_pagesize
                    return queryset[start:end] # 切片后面不能再用order,filter方法，一般在最后的结果再切片
        return None


class WorkbookFileViewSet(viewsets.ModelViewSet):
    serializer_class = WorkbookFileSerializer

    def get_queryset(self):
        return WorkbookFile.objects.filter(workbook_id=self.kwargs['workbook_pk'])

    def get_serializer_context(self):
        return {'workbook_id': self.kwargs['workbook_pk']}


class GetMaxPage(APIView):
    def get(self, request):
        queryset = Workbook.objects.all()
        wx_session = self.request.query_params.get('wx_session')
        pagesize = self.request.query_params.get('pagesize')
        search = self.request.query_params.get('search').strip()
        if(search):
            queryset = queryset.filter(Q(yh__icontains=search) | Q(tzr__icontains=search) | Q(wx_username__icontains=search) | Q(sbhxt__icontains=search) | Q(gzxxhyy__icontains=search) | Q(clgcsm__icontains=search))
        if(wx_session):
            queryset = queryset.filter(wx_session=wx_session)
        if(pagesize and pagesize.isnumeric()):
            int_pagesize = int(pagesize)
            count = queryset.count()
            max_page = math.ceil(count/int_pagesize)
            return JsonResponse({
                "max_page": max_page,
            })
        return JsonResponse({
            "max_page": None
        })