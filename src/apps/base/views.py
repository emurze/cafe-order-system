from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"
    extra_context = {"selected": "home"}


def error_handler_404(request, exception=None):
    return render(request, "404.html", status=404)
