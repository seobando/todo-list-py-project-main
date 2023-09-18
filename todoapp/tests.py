from django.test import TestCase
from django.urls import reverse
from .models import Todo

class TodoTests(TestCase):
    def setUp(self):
        self.todo = Todo.objects.create(title='Test Todo')

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'Test Todo')

    def test_delete_view(self):
        response = self.client.get(reverse('delete', args=[self.todo.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

        # Assert that the todo object is deleted
        with self.assertRaises(Todo.DoesNotExist):
            Todo.objects.get(id=self.todo.id)