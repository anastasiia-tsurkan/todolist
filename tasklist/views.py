from django.urls import reverse_lazy
from django.views import generic

from .models import Task
from .forms import TaskForm


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
    form_class = TaskForm
    success_url = reverse_lazy("tasklist:index")


class TaskUpdate(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasklist:index")


class TaskDelete(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasklist:index")

