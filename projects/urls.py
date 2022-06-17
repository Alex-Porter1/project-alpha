from django.urls import path, reverse_lazy
from projects.views import ProjectListView


urlpatterns = [
    path("", ProjectListView.as_view(), name="list_projects"),

]
