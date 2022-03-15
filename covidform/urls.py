from os import name
from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views
from .views import TempIntoViewSet, TempintoFileViewSet, OvertimeIntoViewSet, OvertimeIntoFileViewSet

router = routers.DefaultRouter()
router.register("tempintos", TempIntoViewSet, basename='tempintos')
router.register("overtimeintos", OvertimeIntoViewSet, basename='overtimeintos')

tempinto_router = routers.NestedDefaultRouter(
    router, "tempintos", lookup='tempinto')
tempinto_router.register("files", TempintoFileViewSet,
                         basename='tempinto-files')

overtimeinto_router = routers.NestedDefaultRouter(
    router, "overtimeintos", lookup='overtimeinto')
overtimeinto_router.register("files", OvertimeIntoFileViewSet,
                             basename='overtimeinto-files')

urlpatterns = [
    path("", include(router.urls+tempinto_router.urls+overtimeinto_router.urls)),
    path('qj_tempinto/', views.QJTempinto.as_view(), name='qj_tempinto'),
    path('qj_overtimeinto/', views.QJOvertimeInto.as_view(), name='qj_overtimeinto'),
    path('delete_invalid_files/', views.DeleteInvalidFiles.as_view(),
         name='delete_invalid_files'),
]

# urlpatterns = router.urls+tempinto_router.urls
