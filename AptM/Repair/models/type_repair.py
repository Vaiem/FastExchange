from django.db import models


class TypeRepair(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование работы"
    )
    objects = models.Manager()

    class Meta:
        verbose_name = "Тип задачи"
        verbose_name_plural = "Типы задач"

    def __str__(self):
        return self.name