from django.http.response import JsonResponse

# Create your views here.
import math
import json
import os
from pathlib import Path
from django.forms.models import model_to_dict
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime, timedelta
from .models import TempInto, TempintoFile, OvertimeInto, OvertimeIntoFile,Clrc,ClrcFile
from .serializers import TempIntoSerializer, TempintoFileSerializer, OvertimeIntoSerializer,OvertimeIntoFileSerializer,ClrcSerializer,ClrcFileSerializer
from django.conf import settings
from django.db.models import Q


class TempIntoViewSet(viewsets.ModelViewSet):
    serializer_class = TempIntoSerializer

    def get_queryset(self):
        queryset = TempInto.objects.prefetch_related('files').all()
        status = self.request.query_params.get('status')
        days = self.request.query_params.get('days')
        weixinID = self.request.query_params.get('weixinid')
        if(status and status.isnumeric()):
            queryset = queryset.filter(status=status)
        if(days and days.isnumeric()):
            end_date = datetime.today()
            start_date = end_date - timedelta(days=int(days))
            queryset = queryset.filter(
                createtime__range=[start_date, end_date])
        if(weixinID):
            queryset = queryset.filter(weixinID=weixinID)
        return queryset.order_by("-createtime")


class TempintoFileViewSet(viewsets.ModelViewSet):
    serializer_class = TempintoFileSerializer

    def get_queryset(self):
        return TempintoFile.objects.filter(tempinto_id=self.kwargs['tempinto_pk'])

    def get_serializer_context(self):
        return {'tempinto_id': self.kwargs['tempinto_pk']}


class QJTempinto(APIView):
    def get(self, request):
        id = self.request.query_params.get('id')
        status = self.request.query_params.get('status')
        days = self.request.query_params.get('days')
        queryset = TempInto.objects.prefetch_related(
            'files').all().order_by("-createtime")
        if(id and id.isnumeric()):
            queryset = queryset.filter(id=id)
        if(status and status.isnumeric()):
            queryset = queryset.filter(status=status)
        if(days and days.isnumeric()):
            end_date = datetime.today()
            start_date = end_date - timedelta(days=int(days))
            queryset = queryset.filter(
                createtime__range=[start_date, end_date])

        serializer = TempIntoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = json.loads(self.request.body.decode('utf-8'))
        id = data.get("id")
        status = data.get("status")
        if(id and status):
            try:
                TempInto.objects.filter(id=id).update(status=status)
                return JsonResponse(model_to_dict(TempInto.objects.get(id=id)))
            except:
                pass
        return JsonResponse({"status": "error"})


class OvertimeIntoViewSet(viewsets.ModelViewSet):
    serializer_class = OvertimeIntoSerializer

    def get_queryset(self):
        queryset = OvertimeInto.objects.prefetch_related('files').all()
        status = self.request.query_params.get('status')
        days = self.request.query_params.get('days')
        weixinID = self.request.query_params.get('weixinid')
        if(status and status.isnumeric()):
            queryset = queryset.filter(status=status)
        if(days and days.isnumeric()):
            end_date = datetime.today()
            start_date = end_date - timedelta(days=int(days))
            queryset = queryset.filter(
                createtime__range=[start_date, end_date])
        if(weixinID):
            queryset = queryset.filter(weixinID=weixinID)
        return queryset.order_by("-createtime")


class OvertimeIntoFileViewSet(viewsets.ModelViewSet):
    serializer_class = OvertimeIntoFileSerializer

    def get_queryset(self):
        return OvertimeIntoFile.objects.filter(overtimeinto_id=self.kwargs['overtimeinto_pk'])

    def get_serializer_context(self):
        return {'overtimeinto_id': self.kwargs['overtimeinto_pk']}


class QJOvertimeInto(APIView):
    def get(self, request):
        id = self.request.query_params.get('id')
        status = self.request.query_params.get('status')
        days = self.request.query_params.get('days')
        queryset = OvertimeInto.objects.prefetch_related(
            'files').all().order_by("-createtime")
        if(id and id.isnumeric()):
            queryset = queryset.filter(id=id)
        if(status and status.isnumeric()):
            queryset = queryset.filter(status=status)
        if(days and days.isnumeric()):
            end_date = datetime.today()
            start_date = end_date - timedelta(days=int(days))
            queryset = queryset.filter(
                createtime__range=[start_date, end_date])

        serializer = OvertimeIntoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = json.loads(self.request.body.decode('utf-8'))
        id = data.get("id")
        status = data.get("status")
        if(id and status):
            try:
                OvertimeInto.objects.filter(id=id).update(status=status)
                return JsonResponse(model_to_dict(OvertimeInto.objects.get(id=id)))
            except:
                pass
        return JsonResponse({"status": "error"})


class ClrcViewSet(viewsets.ModelViewSet):
    serializer_class = ClrcSerializer

    def get_queryset(self):
        queryset = Clrc.objects.prefetch_related('files').all().order_by("-create_time")
        wx_session = self.request.query_params.get('wx_session')
        pagesize = self.request.query_params.get('pagesize')
        page = self.request.query_params.get('page')
        search = self.request.query_params.get('search')
        if(search):
            queryset = queryset.filter(Q(gcmc__icontains=search) | Q(sgdw__icontains=search) | Q(cphm__icontains=search) | Q(sqly__icontains=search) | Q(dclxrxm__icontains=search) | Q(cx__icontains=search))
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
                    queryset = queryset[start:end] # 切片后面不能再用order,filter方法，一般在最后的结果再切片
        return queryset
       


class ClrcFileViewSet(viewsets.ModelViewSet):
    serializer_class = ClrcFileSerializer

    def get_queryset(self):
        return ClrcFile.objects.filter(clrc_id=self.kwargs['clrc_pk'])

    def get_serializer_context(self):
        return {'clrc_id': self.kwargs['clrc_pk']}


class GetMaxPage(APIView):
    def get(self, request):
        queryset = Clrc.objects.all()
        wx_session = self.request.query_params.get('wx_session')
        pagesize = self.request.query_params.get('pagesize')
        search = self.request.query_params.get('search').strip()
        if(search):
            queryset = queryset.filter(Q(gcmc__icontains=search) | Q(sgdw__icontains=search) | Q(cphm__icontains=search) | Q(sqly__icontains=search) | Q(dclxrxm__icontains=search) | Q(cx__icontains=search))
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

class QJClrc(APIView):
    def get(self, request):
        id = self.request.query_params.get('id')
        status = self.request.query_params.get('status')
        days = self.request.query_params.get('days')
        queryset = Clrc.objects.prefetch_related(
            'files').all().order_by("-create_time")
        if(id and id.isnumeric()):
            queryset = queryset.filter(id=id)
        if(status and status.isnumeric()):
            queryset = queryset.filter(status=status)
        if(days and days.isnumeric()):
            end_date = datetime.today()
            start_date = end_date - timedelta(days=int(days))
            queryset = queryset.filter(
                createtime__range=[start_date, end_date])

        serializer = ClrcSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = json.loads(self.request.body.decode('utf-8'))
        id = data.get("id")
        status = data.get("status")
        if(id and status):
            try:
                Clrc.objects.filter(id=id).update(status=status)
                return JsonResponse(model_to_dict(Clrc.objects.get(id=id)))
            except:
                pass
        return JsonResponse({"status": "error"})


class DeleteInvalidFiles(APIView):
    # 删除无效的图片：数据库信息已删除，文件系统还存在的
    def post(self, request):
        dir1 = os.path.join(settings.MEDIA_ROOT, "covid19")
        path1 = Path(dir1)
        files1 = [p for p in path1.iterdir()]
        del_count1 = 0
        for file1 in files1:
            if not TempintoFile.objects.filter(file__contains=file1.name).exists():
                os.remove(file1.absolute())
                del_count1 += 1

        dir2 = os.path.join(settings.MEDIA_ROOT, "covid19_OT")
        path2 = Path(dir2)
        files2 = [p for p in path2.iterdir()]
        del_count2 = 0
        for file2 in files2:
            if not OvertimeIntoFile.objects.filter(file__contains=file2.name).exists():
                os.remove(file2.absolute())
                del_count2 += 1
        
        dir3 = os.path.join(settings.MEDIA_ROOT, "clrc")
        path3 = Path(dir3)
        files3 = [p for p in path3.iterdir()]
        del_count3 = 0
        for file3 in files3:
            if not ClrcFile.objects.filter(file__contains=file3.name).exists():
                os.remove(file3.absolute())
                del_count3 += 1

        return JsonResponse({
            "del_tempinto": del_count1,
            "del_overtimeinto": del_count2,
            "del_clrc": del_count3,
        })
