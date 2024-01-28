from apps.reobjects import models


# Create your models here.
class Place(models.place.Place):
    def __str__(self):
        return f"{self.city}, {self.street}, {self.house}, {self.tag}, {self.flat}"

    class Meta:
        proxy = True
        verbose_name = "Место"
        verbose_name_plural = "Места"


class City(models.place.City):
    def __str__(self):
        return self.name

    class Meta:
        proxy = True
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Coordinates(models.place.Coordinates):
    def __str__(self):
        return f"{self.ydx_latitude}  ,  {self.ydx_longitude}"

    class Meta:
        proxy = True
        verbose_name = "Координаты"
        verbose_name_plural = "Координаты"


class Country(models.place.Country):
    def __str__(self):
        return self.name

    class Meta:
        proxy = True
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class District(models.place.District):
    def __str__(self):
        return self.name

    class Meta:
        proxy = True
        verbose_name = "Район"
        verbose_name_plural = "Районы"


class Region(models.place.Region):
    def __str__(self):
        return self.name

    class Meta:
        proxy = True
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"


class Street(models.place.Street):
    def __str__(self):
        return self.name

    class Meta:
        proxy = True
        verbose_name = "Улица"
        verbose_name_plural = "Улицы"


class Tag(models.place.Tag):
    def __str__(self):
        return self.name

    class Meta:
        proxy = True
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
