from django.urls import path
from .views import TodoList,TodoDetails


urlpatterns=[
    path("task/",TodoList.as_view()),
    path("task/<int:pk>",TodoDetails.as_view())
]