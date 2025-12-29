from rest_framework.views import APIView
from rest_framework .response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer, TaskDetailsSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


User = get_user_model()

class AllTaskView(APIView):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.filter(user=request.user).order_by('-date_created')
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

class TaskDetailsView(APIView):
    def get(self, request, slug=None, *args, **kwargs):
        task = get_object_or_404(Task, slug=slug, user=request.user)    
        serializer = TaskDetailsSerializer(task)
        return Response(serializer.data)

class SearchTaskView(APIView):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')
        show_all = request.GET.get("full") == "1"

        qs = Task.objects.filter(user=request.user).search(query=query) if query else Task.objects.none()
        search_task_list = qs if show_all else qs[:5]
        serializer = TaskSerializer(search_task_list, many=True)

        return Response({
            "results": serializer.data,
            "query": query,
            "total_count": qs.count(),
            "show_all": show_all
        })

class AddTaskView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateTaskView(APIView):
    def patch(self, request, id, *args, **kwargs):
        task = get_object_or_404(Task, id=id, user=request.user)
        serializer = TaskDetailsSerializer(task, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteTaskView(APIView):
    def delete(self, request, id, *args, **kwargs):
        task = get_object_or_404(Task, id=id, user=request.user)
        task.delete()
        return Response({"message": f"Task '{task.title}' deleted successfully"}, status=status.HTTP_204_NO_CONTENT)