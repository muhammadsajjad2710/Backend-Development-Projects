from django.db import models

class ShortLink(models.Model):
    code = models.SlugField(unique=True)
    url = models.URLField()
