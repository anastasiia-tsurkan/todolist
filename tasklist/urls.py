from django.urls import path

from tasklist.views import index

urlpatterns = [
    path("", index, name="index"),
]
