from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Task


class TaskCreateTestCase(APITestCase):

    def test_task_create(self):
        response = self.client.post(reverse('create_task'), {
            'name': 'test',
            'description': 'test'},
            format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().name, 'test')


class TaskListRetreiveUpdateDeleteTestCase(APITestCase):

    def setUp(self):
        task = Task(name='test', description='test')
        task.save()

    def test_task_list(self):
        response = self.client.get(reverse('list_tasks'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'test')

    def test_task_retreive(self):
        response = self.client.get(reverse('retrieve_update_destroy_task',
                                   kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'test')

    def test_task_update(self):
        response = self.client.put(reverse('retrieve_update_destroy_task',
                                   kwargs={'pk': 1}),
                                   {'name': 'test2', 'description': 'test2'},
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().name, 'test2')

    def test_task_delete(self):
        response = self.client.delete(reverse('retrieve_update_destroy_task',
                                      kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
