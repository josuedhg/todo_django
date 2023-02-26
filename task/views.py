from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.serializers import ModelSerializer

from .models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class ListTasks(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CreateTask(CreateAPIView):
    serializer_class = TaskSerializer


class RetrieveUpdateDestroyTask(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
