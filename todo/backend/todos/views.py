from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

class ListTodo(generics.ListAPIView):# to display all todos
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveAPIView):# to display a single model instance(1 todo)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer