import json

from django.http import HttpResponse, JsonResponse
from django.template import loader
from ..models.objects_re import ReObjectImage


def index(request, uuid):
    images_objs = [
        obj for obj in ReObjectImage.objects.filter(objectModel__uuid=uuid).values()
    ]
    template = loader.get_template("front/pages/sort_photos/index.html")
    print(images_objs)
    context = {
        "re_object_uuid": uuid,
        "images_objs": images_objs,
    }
    return HttpResponse(template.render(context, request))


def update_values(request):
    if request.method == "POST":
        raw_body = request.body
        json_data = json.loads(raw_body)
        new_order: dict = json_data["images"]
        old_order = {
            str(obj["uuid"]): obj["order"]
            for obj in ReObjectImage.objects.filter(
                objectModel__uuid=json_data["re_object_id"]
            ).values()
        }

        for uuid, order in new_order.items():
            obj = ReObjectImage.objects.get(uuid=uuid)
            obj.order = order
            obj.save()
        print(old_order)
        print(new_order)
        return JsonResponse({"message": "Values updated successfully"})
    else:
        return JsonResponse({"error": "Invalid request method"})
