from django.contrib import admin

from .models import Tag, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("content", "datetime", "deadline", "status")


admin.site.register(Tag)
