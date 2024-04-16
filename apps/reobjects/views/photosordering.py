import json

from django.http import HttpResponse, JsonResponse
from django.template import loader
from ..models.objects_re import ReObjectImage


def index(request, uuid):
    images = [
        obj
        for obj in ReObjectImage.objects.filter(objectModel__uuid=uuid).values_list(
            "image",
            flat=True,
        )
    ]
    template = loader.get_template("front/pages/sort_photos/index.html")
    print(images)
    context = {
        "images": images,
    }
    return HttpResponse(template.render(context, request))


def update_values(request):
    if request.method == "POST":
        raw_body = request.body
        json_data = json.loads(raw_body)
        print(json_data)
        return JsonResponse({"message": "Values updated successfully"})
    else:
        return JsonResponse({"error": "Invalid request method"})
