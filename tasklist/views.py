from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from .forms import TaskForm, TagForm
from .models import Task, Tag


class TaskList(generic.ListView):
    model = Task
    context_object_name = "tasks_list"
    template_name = "tasklist/index.html"
    queryset = Task.objects.prefetch_related("tags")


class TaskCompletionView(View):
    def post(self, request, **kwargs):
        task = Task.objects.get(id=kwargs["pk"])

        task.status = request.POST.get("complete", not task.status)
        # action = self.request.POST.get()
        # if action:
        #     task.status = not task.status

        task.save()
        return redirect("tasklist:index")
        # return render(request, "tasklist/index.html", {"task": task})


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


# class TaskComplete(generic.ListView):
#     model = Task
#
#     def post(self, request, **kwargs):
#         task = Task.objects.get(id=kwargs["pk"])
#
#         action = self.request.POST.get("task_status")
#         if action:
#             task.status = not task.status
#
#         task.save()
#
#         return render(request, "tasklist/index.html", {"task": task})


    def get_object(self, queryset=None):
        task = super().get_object()
        task.status = not task.status
        return task

# def toggle_complete_task(request, pk) -> HttpResponseRedirect:
#     task = Task.objects.get(id=pk)
#     if task.status:
#         task.status = False
#     else:
#         task.status = True
#     task.save()
#     return HttpResponseRedirect(reverse_lazy("tasklist:index"))
