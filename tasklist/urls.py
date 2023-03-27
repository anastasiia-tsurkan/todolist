from django.urls import path

from tasklist.views import (
    TaskList,
    TaskCreate,
    TaskUpdate,
    TaskDelete,
    TagList,
    TagCreate,
    TagUpdate,
    TagDelete
)

urlpatterns = [
    path("", TaskList.as_view(), name="index"),
    path("create/", TaskCreate.as_view(), name="task-create"),
    path("<int:pk>/update/", TaskUpdate.as_view(), name="task-update"),
    path("<int:pk>/delete/", TaskDelete.as_view(), name="task-delete"),
    path("tags/", TagList.as_view(), name="tags-list"),
    path("tags/create/", TagCreate.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdate.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDelete.as_view(), name="tag-delete")
]

app_name = "tasklist"
