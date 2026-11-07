from django.db import models

class Issue(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    open = models.BooleanField(default=True)
