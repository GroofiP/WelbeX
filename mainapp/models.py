from django.db import models


class TableWebix(models.Model):
    data = models.DateField(verbose_name="Дата", auto_now_add=True)
    name = models.CharField(max_length=128, verbose_name="Название")
    amount = models.PositiveSmallIntegerField(verbose_name="Количество")
    distance = models.PositiveIntegerField(verbose_name="Расстояние")

    def __str__(self):
        return self.name
