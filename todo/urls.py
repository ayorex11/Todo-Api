from django.urls import path
from . import views

urlpatterns = [
    path("tasks/", views.get_tasks),
    path("tasks/stats/", views.productivity_stats),
    path("tasks-detail/<str:pk>/", views.TaskDetail),
    path("create/", views.create),
    path("tasks-update/<str:pk>/", views.update),
    path("tasks-delete/<str:pk>/", views.DeleteTodo),
]
