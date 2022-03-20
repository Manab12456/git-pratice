from django.shortcuts import get_object_or_404, render
from .models import Tasks
from .serializers import TasksSerializer,TasksSerializer2
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework import status

#class based views:
class TasksModelViewSet(viewsets.ModelViewSet):
    queryset= Tasks.objects.all()
    serializer_class = TasksSerializer

class TasksModelGenericView(generics.ListCreateAPIView):
    queryset= Tasks.objects.all()
    serializer_class = TasksSerializer

class TasksModelGenericView2(generics.RetrieveUpdateDestroyAPIView):
    queryset= Tasks.objects.all()
    serializer_class = TasksSerializer

class TasksAPIViewSet(APIView):
    def get(self, request, *args, **kwargs):
        tasks_objects = Tasks.objects.all()
        tasks_serializer_data= TasksSerializer(tasks_objects, many =True)
        return Response(tasks_serializer_data.data, status=status.HTTP_200_OK)

    def patch(self,request,id=None):
        tasks_objects = Tasks.objects.get(id=id)
        tasks_serializer_data= TasksSerializer(tasks_objects,data=request.data, partial=True)
        if tasks_serializer_data.is_valid():
            tasks_serializer_data.save()
            return Response({"status": "success", "data":tasks_serializer_data.data})
        else:
            return Response({"status": "error", "data": tasks_serializer_data.errors})

    def post(self, request, *args, **kwargs):
        data={
            'type': request.data.get(),
            'title': request.data.get(),
            'description': request.data.get(),
            'due_date': request.data.get(),
            'remainder': request.data.get(),
            'created_at': request.data.get(),
            'finised': request.data.get(),
        }
        tasks_serializer_data=TasksSerializer(data=data)
        if tasks_serializer_data.is_valid():
            tasks_serializer_data.save()
            return Response(tasks_serializer_data, status=status.HTTP_201_CREATED)
        return Response(tasks_serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id=None):
        tasks_objects =get_object_or_404(Tasks,id=id)
        tasks_objects.delete()
        return Response({"status":"success","data":"Item Deleted"})

