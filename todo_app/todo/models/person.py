from django.db import models


class Person(models.Model):
    name = models.CharField(
        max_length=20,
        null=True,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "people"
        