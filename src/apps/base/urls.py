from django.urls import path

from apps.base.views import (
    HomeView,
    error_handler_404,
    error_handler_500,
    error_handler_403,
    error_handler_400,
)

handler404 = error_handler_404
handler500 = error_handler_500
handler403 = error_handler_403
handler400 = error_handler_400

app_name = "base"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]
