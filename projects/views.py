from django.shortcuts import render
from projects.models import Project
from django.views.generic.list import ListView
# Create your views here.


class ProjectListView(ListView):
    model = Project
    template_name = "projects/list.html"
    context_object_name = "projectslist"