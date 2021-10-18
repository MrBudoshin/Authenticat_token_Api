from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="title")
    description = models.TextField(verbose_name="description")
    data = models.DateTimeField(auto_now_add=True, verbose_name="data")

