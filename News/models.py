from django.db import models

class NewsArticle(models.Model):
    source_id = models.CharField(max_length=255, default=None)
    source_name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField(primary_key=True)
    url_to_image = models.URLField()
    published_at = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return self.title
