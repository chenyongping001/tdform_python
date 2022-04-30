# from asyncio.windows_events import NULL
from contextlib import nullcontext
import requests
import hashlib
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.conf import settings
from wxauth.models import WXUser,HfWxUser

# Create your views here.


def index(request):
    return HttpResponse("Hello world.")


def wx_auth(request, code):
    wxapi = "https://api.weixin.qq.com/sns/jscode2session?appid={AppId}&secret={AppSecret}&js_code={code}&grant_type=authorization_code".format(
        AppId=settings.WX_MINIPROGRAM_APPID,
        AppSecret=settings.WX_MINIPROGRAM_SECRET_KEY,
        code=code
    )
    try:
        response = requests.get(wxapi)
        if(response.json().get('openid') == None):
            raise Exception()
    except Exception:
        return JsonResponse({"session": None})

    openid = response.json().get('openid')
    hashdata = hashlib.md5()
    hashdata.update(bytes(openid, encoding='utf-8'))
    session = hashdata.hexdigest()
    data = {
        "session": session,
    }
    if(not WXUser.objects.filter(openid=openid)):
        WXUser.objects.create(openid=openid, session=session)
    return JsonResponse(data)


def wx_getHfWxUser(request,code,session):
    wxapi_get_access_token = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={AppId}&secret={AppSecret}".format(
        AppId=settings.WX_MINIPROGRAM_APPID,
        AppSecret=settings.WX_MINIPROGRAM_SECRET_KEY
    )
    try:
        response = requests.get(wxapi_get_access_token)
        if(response.json().get('access_token') == None):
            raise Exception()
    except Exception:
        return JsonResponse({"phone_info": None})

    access_token = response.json().get('access_token')
    wxapi_get_phonenumber = "https://api.weixin.qq.com/wxa/business/getuserphonenumber?access_token={ACCESS_TOKEN}".format(
        ACCESS_TOKEN=access_token
    )

    # 重要！，一定要传 json={'code': code}，如果传data={'code': code}将出错，折腾了不少时间
    response = requests.post(
        wxapi_get_phonenumber,
        json={'code': code}
    )


    if(response.json().get('errcode') == 0):
        phone_number = response.json().get('phone_info').get('phoneNumber')
        wx_user = WXUser.objects.filter(session=session).first()
        hf_user = HfWxUser.objects.filter(phone_number=phone_number).first()
        if(wx_user):
            wx_user.phone_number = phone_number
            wx_user.save()
            if(hf_user):
                return JsonResponse({"wx_username": hf_user.username})

        return JsonResponse({"wx_username": None})
    return JsonResponse({"phone_info": None})

def wx_getUserFromSession(request,session):
    wx_user = WXUser.objects.filter(session=session).first()
    if(wx_user and wx_user.phone_number):
        hf_user = HfWxUser.objects.filter(phone_number=wx_user.phone_number).first()
        if(hf_user):
            return JsonResponse({"wx_username": hf_user.username})
    return JsonResponse({"wx_username": None})