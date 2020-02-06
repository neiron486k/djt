from django.db import models


class Page(models.Model):
    slug = models.CharField(max_length=50, db_index=True, unique=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.slug

    class Meta:
        db_table = 'pages'
        ordering = ['id']
