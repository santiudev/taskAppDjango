from rest_framework.response import Response
from rest_framework.decorators import api_view
from tasks import serializers
##My imports
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def getTask(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many=True)
    return Response(serializer.data)

    
@api_view(['POST'])
def postTask(request):
    data = request.data
    task = Task.objects.create(
        user = data['user'],
        title = data['title'],
        description = data['description'],
        is_completed = data['is_completed'],
        priority = data['priority']
    )
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def putTask(request, pk):
    data= request.data
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Task eliminated')