from django.views.generic.edit import CreateView, UpdateView
from tasks.models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.list import ListView

# Create your views here.


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/create.html"
    context_object_name = "taskscreate"
    fields = ["name", "start_date", "due_date", "project", "assignee"]

    def get_success_url(self):
        new_id = self.object.project.id
        return reverse_lazy("show_project", kwargs={"pk": new_id})


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/list.html"
    context_object_name = "taskslist"

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)


class TaskUpdateView(UpdateView):
    model = Task
    template_name = "tasks/update.html"
    context_object_name = "tasksupdate"
    fields = ["is_completed"]
    success_url = reverse_lazy("show_my_tasks")
