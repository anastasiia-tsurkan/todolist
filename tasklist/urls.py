from django.urls import path

from tasklist.views import TaskList

urlpatterns = [
    path("", TaskList.as_view(), name="index"),
]

app_name = "tasklist"
