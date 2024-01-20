from django.urls import path
from .views import MenListView, MenDetailView


urlpatterns = [
   path("BookList/", MenListView.as_view(), name="book-list-data"),
   path("bookList/<int:pk>/", MenDetailView.as_view(), name="book-list-details"),
]
