from django.db import models


class Pages(models.Model):
    title = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=255, null=True)
    keywords = models.CharField(max_length=255, null=True)
    content = models.TextField()
    slug = models.CharField(max_length=50, db_index=True, unique=True)

    class Meta:
        ordering = ['id']
