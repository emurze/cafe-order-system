from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.base.urls", namespace="base")),
    path("orders/", include("apps.orders.urls", namespace="orders")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )
