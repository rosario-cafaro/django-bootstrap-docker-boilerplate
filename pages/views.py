from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("pages/index.html")
    context = {
        'active_link': 'home',
    }
    return HttpResponse(template.render(context, request))


def about(request):
    context = {
        'active_link': 'about',
    }
    return render(request, "pages/about.html", context)
