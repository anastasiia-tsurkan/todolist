from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True)
    status = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tags")

    def __str__(self):
        return self.content
