from apps.reobjects.models.objects_re import (
    ReObjectEngineeringServices,
    ReObject,
    ReObjectImage,
)


# Create your models here.
class ReObjectProxy(ReObject):
    def __str__(self):
        return f"{self.uuid}"

    class Meta:
        proxy = True
        verbose_name = "Объект"
        verbose_name_plural = "Объекты"


class ReObjectImageProxy(ReObjectImage):
    def __str__(self):
        return f"{self.uuid}"

    class Meta:
        proxy = True
        verbose_name = "Фото объекта"
        verbose_name_plural = "Фото объектов"


class ReObjectEngineeringServicesProxy(ReObjectEngineeringServices):
    def __str__(self):
        return "ReObjectImage"

    class Meta:
        proxy = True
        verbose_name = "Коммуникации объекта"
        verbose_name_plural = "Коммуникации объектов"
