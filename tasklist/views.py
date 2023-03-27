from django.views import generic

from .models import Task, Tag


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
