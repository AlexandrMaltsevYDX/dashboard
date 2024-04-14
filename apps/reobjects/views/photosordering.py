from django.http import HttpResponse
from django.template import loader


def index(request):
    order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    template = loader.get_template("front/pages/sort_photos/index.html")
    context = {
        "order": order,
    }
    return HttpResponse(template.render(context, request))
