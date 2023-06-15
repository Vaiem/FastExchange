from django.db import models
from django.urls import reverse

class Status(models.TextChoices):
     #Статусы для заявок
    CREATED = 'CREATED', 'Новая заявка от клиента'
    CONFIRMED = 'CONFIRMED', 'Подтверждена техником'
    READY_TO_WORK = 'READY_TO_WORK', 'Готова к работе'
    PROGRESS = 'PROGRESS', 'В работе'
    VERIFICATION = 'VERIFICATION', 'Ремонт выполнен'
    TESTS = 'TESTS', 'На тестировании'
    RE_REPAIR = 'RE_REPAIR', 'На доработку'


class Repair(models.Model):
    user = models.ManyToManyField(to="users.User", related_name="repair", verbose_name="все участники")

    description = models.TextField(verbose_name="Описание поломки")

    status = models.CharField(
        max_length=25,
        choices=Status.choices,
        default=Status.CREATED,
    )

    work = models.ManyToManyField(to="Repair.Work", related_name="work_repairs", verbose_name="работы")

    type_repair = models.ForeignKey(
        "Repair.TypeRepair", related_name="type_repairs",
        on_delete=models.PROTECT, verbose_name="Тип Работ",
        null=True, blank=True
    )

    objects = models.Manager()

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f"Заявка - {self.id}, статус - {self.status}"

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})