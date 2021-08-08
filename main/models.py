from django.db import models


class FAQ(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Blogs(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    video_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
