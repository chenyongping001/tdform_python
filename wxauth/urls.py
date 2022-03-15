from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:code>', views.wx_auth, name='wx_auth'),
    path('wx_getPhoneNumber/<str:code>/',
         views.wx_getPhoneNumber, name='wx_getPhoneNumber'),
]
