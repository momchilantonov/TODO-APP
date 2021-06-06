from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=10,
        null=True,
    )

    def __str__(self):
        return f"{self.id}: {self.name}"

    class Meta:
        verbose_name_plural = "categories"