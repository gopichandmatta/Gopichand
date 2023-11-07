from django.urls import path
from .views import TodoItemListCreateView, TodoItemDetailView

urlpatterns = [
    path('todo items/', TodoItemListCreateView.as_view(), name='todo-item-list'),
    path('todo items/<int:pk>/', TodoItemDetailView.as_view(), name='todo-item-detail'),
]