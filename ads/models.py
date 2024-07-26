from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок", help_text="Укажите заголовок")
    ad_id = models.PositiveIntegerField(unique=True, verbose_name="ID обьявления", help_text="Укажите ID обьявления")
    author = models.CharField(max_length=100, verbose_name="Автор обьявления", help_text="Укажите автора обьявления")
    views_count = models.PositiveIntegerField(editable=False, verbose_name="Колличество просмотров")
    position = models.PositiveIntegerField(verbose_name="Позиция обьявления", help_text="Укажите позицию, на которой стоит обьявление")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Обьявление"
        verbose_name_plural = "Обьявления"
