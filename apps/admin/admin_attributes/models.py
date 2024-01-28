from django.db import models
from apps.reobjects.models.attributes import (
    Category,
    TypeHouse,
    WindowsOrientation,
    Ownership,
    LandCategory,
    ReliefArea,
    Fencing,
    Foundation,
    WallMaterial,
    EngineeringServices,
    VillageFences,
    ObjectDescription,
)


# Create your models here.
class Category(Category):
    def __str__(self):
        return self.name

    class Meta:
        proxy = True
        verbose_name = "Категория объекта"
        verbose_name_plural = "Категория объекта"


class EngineeringServices(EngineeringServices):
    def __str__(self):
        return self.value

    class Meta:
        proxy = True
        verbose_name = "Инженерные сети"
        verbose_name_plural = "Инженерные сети"


class Fencing(Fencing):
    def __str__(self):
        return self.value

    class Meta:
        proxy = True
        verbose_name = "Ограждение участка"
        verbose_name_plural = "Ограждение участка"


class Foundation(Foundation):
    def __str__(self):
        return self.value

    class Meta:
        proxy = True
        verbose_name = "Тип фундамента"
        verbose_name_plural = "Тип фундамента"


class LandCategory(LandCategory):
    def __str__(self):
        return self.value

    class Meta:
        proxy = True
        verbose_name = "Категория земель"
        verbose_name_plural = "Категория земель"


class ObjectDescription(ObjectDescription):
    def __str__(self):
        return self.value[:25]

    class Meta:
        proxy = True
        verbose_name = "Описание объекта"
        verbose_name_plural = "Описание объекта"


class Ownership(Ownership):
    def __str__(self):
        return self.value

    class Meta:
        proxy = True
        verbose_name = "Тип собственности"
        verbose_name_plural = "Тип собственности"


class ReliefArea(ReliefArea):
    def __str__(self):
        return self.value

    class Meta:
        proxy = True
        verbose_name = "Рельеф участка"
        verbose_name_plural = "Рельеф участка"


class TypeHouse(TypeHouse):
    def __str__(self):
        return self.name

    class Meta:
        proxy = True
        verbose_name = "Тип объекта"
        verbose_name_plural = "Тип объекта"


class VillageFences(VillageFences):
    def __str__(self):
        return self.value

    class Meta:
        proxy = True
        verbose_name = "Ограждения в поселке"
        verbose_name_plural = "Ограждения в поселке"


class WallMaterial(WallMaterial):
    def __str__(self):
        return self.value

    class Meta:
        proxy = True
        verbose_name = "Материал стен"
        verbose_name_plural = "Материал стен"


class WindowsOrientation(WindowsOrientation):
    def __str__(self):
        return self.value

    class Meta:
        proxy = True
        verbose_name = "Ориентация окон"
        verbose_name_plural = "Ориентация окон"
