from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import status


class HomeView(TemplateView):
    template_name = "base/home.html"
    extra_context = {"selected": "home"}


def error_handler_404(request: WSGIRequest, exception) -> HttpResponse:
    return render(
        request,
        "base/errors/404.html",
        status=status.HTTP_404_NOT_FOUND,
    )


def error_handler_500(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        "base/errors/500.html",
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


def error_handler_403(request: WSGIRequest, exception) -> HttpResponse:
    return render(
        request,
        "base/errors/403.html",
        status=status.HTTP_403_FORBIDDEN,
    )


def error_handler_400(request: WSGIRequest, exception) -> HttpResponse:
    return render(
        request,
        "base/errors/400.html",
        status=status.HTTP_400_BAD_REQUEST,
    )
