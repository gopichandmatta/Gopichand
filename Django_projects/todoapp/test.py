from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import TodoItem
import json


class TodoItemTests(APITestCase):
    def setUp(self):
        self.item_data = {
            "title": "Test Item",
            "description": "Test description",
            "completed": False
        }
        self.item = TodoItem.objects.create(**self.item_data)
        self.url = reverse("todo-item-list")

    def test_list_todo_items(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_todo_item(self):
        data = {
            "title": "New Item",
            "description": "New description",
            "completed": False
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_todo_item(self):
        url = reverse("todo-item-detail", args=[self.item.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_todo_item(self):
        url = reverse("todo-item-detail", args=[self.item.id])
        updated_data = {
            "title": "Updated Item",
            "description": "Updated description",
            "completed": True
        }
        response = self.client.put(url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_todo_item(self):
        url = reverse("todo-item-detail", args=[self.item.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(TodoItem.objects.filter(id=self.item.id).exists())