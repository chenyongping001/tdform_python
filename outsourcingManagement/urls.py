from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from .views import WorkbookViewSet,WorkbookFileViewSet

router = routers.DefaultRouter()
router.register("workbooks", WorkbookViewSet, basename='workbooks')

workbook_router = routers.NestedDefaultRouter(
    router, "workbooks", lookup='workbook')
workbook_router.register("files", WorkbookFileViewSet,
                         basename='workbook-files')

urlpatterns = [
    path("", include(router.urls + workbook_router.urls)),
]

# urlpatterns = router.urls+tempinto_router.urls