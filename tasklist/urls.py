from django.urls import path

from tasklist.views import TaskList, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
    path("", TaskList.as_view(), name="index"),
    path("create/", TaskCreate.as_view(), name="task-create"),
    path("<int:pk>/update/", TaskUpdate.as_view(), name="task-update"),
    path("<int:pk>/delete/", TaskDelete.as_view(), name="task-delete")
]

app_name = "tasklist"
