from django.db import models


class Abstract(models.Model):

    modtime = models.DateTimeField(auto_now=False)
    addtime = models.DateTimeField(auto_now_add=False)

    class Meta:
        abstract = True
        verbose_name = None
        verbose_name_plural = None

    def get_absolute_url(self):
        raise NotImplementedError()
