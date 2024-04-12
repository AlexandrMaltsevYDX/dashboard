from django.http import HttpResponse
from django.template import loader


def index(request):
    test = "test"
    template = loader.get_template("front/pages/sort_photos/index.html")
    context = {
        "g": test,
    }
    return HttpResponse(template.render(context, request))
