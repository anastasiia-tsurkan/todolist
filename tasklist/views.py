from django.urls import reverse_lazy
from django.views import generic

from .models import Task, Tag
from .forms import TaskForm, TagForm


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


class TagList(generic.ListView):
    model = Tag
    context_object_name = "tags_list"
    template_name = "tasklist/tags_list.html"
    queryset = Tag.objects.all()


class TagCreate(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("tasklist:tags-list")


class TagUpdate(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("tasklist:tags-list")


class TagDelete(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasklist:tags-list")
