import json

from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.utils.http import urlencode

from ..models.objects_re import ReObjectImage, ReObjectPlanModel, ReObject
from apps.village.models.village import VillageImageModel, VillagePlanModel, Village

MODELSDICT = {
    "reobjectproxy": {
        "photo": ReObjectImage,
        "plans": ReObjectPlanModel,
        "model": ReObject,
    },
    "villageproxy": {
        "photo": VillageImageModel,
        "plans": VillagePlanModel,
        "model": Village,
    },
}

IMAGETYPES = {
    "photo": "Фото",
    "plans": "Планы",
}


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


def sorting(request, **kwargs):
    model = MODELSDICT[kwargs["model"]][kwargs["imagetype"]]
    object_model = MODELSDICT[kwargs["model"]]["model"].objects.get(uuid=kwargs["uuid"])
    images_objs = [
        obj
        for obj in model.objects.filter(objectModel__uuid=kwargs["uuid"])
        .order_by("order")
        .values()
    ]
    template = loader.get_template("front/pages/sort_photos/index.html")
    object_fields = [
        ("uuid", object_model.uuid, "uuid объекта в БД :"),
        ("id", object_model.id, "ID объекта :"),
        ("name", object_model.name, "Имя объекта :"),
        ("place", object_model.place, "Адресс :"),
        (
            "image_type",
            IMAGETYPES[kwargs["imagetype"]],
            "Тип изображений(фото/планы) :",
        ),
    ]
    context = {
        "re_object_uuid": kwargs["uuid"],
        "object_fields": object_fields,
        "images_objs": images_objs,
    }
    return HttpResponse(template.render(context, request))


def update_values(request, **kwargs):
    print(kwargs)
    model = MODELSDICT[kwargs["model"]][kwargs["imagetype"]]
    uuid = kwargs["uuid"]

    if request.method == "POST":
        raw_body = request.body
        json_data = json.loads(raw_body)
        new_order: dict = json_data["images"]
        old_order = {
            str(obj["uuid"]): obj["order"]
            for obj in model.objects.filter(
                objectModel__uuid=json_data["re_object_id"]
            ).values()
        }

        for uuid, order in new_order.items():
            obj = model.objects.get(uuid=uuid)
            obj.order = order
            obj.save()
        print(old_order)
        print(new_order)
        return JsonResponse({"message": "Values updated successfully"})
    else:
        return JsonResponse({"error": "Invalid request method"})
