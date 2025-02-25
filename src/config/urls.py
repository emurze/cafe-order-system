from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from apps.base.views import (
    error_handler_404,
    error_handler_500,
    error_handler_403,
    error_handler_400,
)
from config import settings

handler404 = error_handler_404
handler500 = error_handler_500
handler403 = error_handler_403
handler400 = error_handler_400

urlpatterns = [
    path("api/v1/", include("apps.orders.api_urls", namespace="orders_api")),
    path("admin/", admin.site.urls),
    path("", include("apps.base.urls", namespace="base")),
    path("orders/", include("apps.orders.urls", namespace="orders")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )
