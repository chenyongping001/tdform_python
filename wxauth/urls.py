from django.urls import path
from rest_framework import routers

from outsourcingManagement import urls
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:code>', views.wx_auth, name='wx_auth'),
    path('wx_getHfWxUser/<str:code>/<str:session>',
         views.wx_getHfWxUser, name='wx_getHfWxUser'),
    path('wx_getUserFromSession/<str:session>',
         views.wx_getUserFromSession, name='wx_getUserFromSession'),
    path('useful_totp/',
         views.UsefulTotp.as_view(), name='useful_totp'),

]

router = routers.SimpleRouter()
router.register('totps', views.TOTPViewSet, basename='totps')
urlpatterns += router.urls