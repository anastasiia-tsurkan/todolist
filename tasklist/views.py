from django.urls import reverse_lazy
from django.views import generic

from .models import Task


# def index(request):
#     return render(
#         request,
#         "tasklist/index.html"
#     )

class TaskList(generic.ListView):
    model = Task
    context_object_name = "tasks_list"
    template_name = "tasklist/index.html"
    queryset = Task.objects.prefetch_related("tags")


class TaskCreate(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasklist:index")


class TaskUpdate(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasklist:index")


class TaskDelete(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasklist:index")

