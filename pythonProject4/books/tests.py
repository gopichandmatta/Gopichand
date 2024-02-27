from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Book


class BookTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book_data = {'title': 'Test Book', 'author': 'Test Author', 'publication_date': '2023-01-01'}
        self.book = Book.objects.create(**self.book_data)
        self.url = reverse('book-list')

    def test_get_books(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 1)

    def test_create_book(self):  # creating
        response = self.client.post(self.url, self.book_data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Book.objects.count(), 2)

    def test_get_book_detail(self):
        detail_url=reverse('book-detail', args=[self.book.id])
        response = self.client.get(detail_url)
        self.assertEquals(response.status_code,status.HTTP_200_OK)
        self.assertEquals(response.data['title'],self.book_data['title'])

    def test_update_book(self):
        update_data = {'title': 'Updated Book', 'author': 'Updated Author', 'publication_date': '2023-01-02'}
        detail_url = reverse('book-detail', args=[self.book.id])
        response = self.client.put(detail_url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(id=self.book.id).title, update_data['title'])

    def test_delete_book(self):
        detail_url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)