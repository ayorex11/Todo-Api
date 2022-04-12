from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import TodoSerializer
from drf_yasg.utils import swagger_auto_schema


from todo.models import Todo


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_tasks(request):
    user = request.user
    dates = user.tasks.all().values_list("date",flat=True).distinct()
    
    data = {str(date): user.tasks.filter(date=date).values() for date in dates} 
    
    return Response(data, status=status.HTTP_200_OK)
    
    
@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def productivity_stats(request):
    user = request.user
    
    data = {"pending": user.tasks.filter(status="pending").count(),
            "completed": user.tasks.filter(status="completed").count()}
    
    return Response(data, status=status.HTTP_200_OK)

@swagger_auto_schema(methods=["POST"], request_body=TodoSerializer())
@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def create(request):
    user = request.user
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
   
                                                         
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def TaskDetail(request, pk):
    user = request.user
    tasks = Todo.objects.get(id=pk)
    serializer = TodoSerializer(tasks, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(methods=["POST"], request_body=TodoSerializer())
@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def update(request, pk):
    user = request.user
    task = Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
   
                                                         
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def DeleteTodo(request, pk):
    user = request.user 
    task = Todo.objects.get(id=pk)
    task.delete()

    return Response('Item successfully deleted!', status=status.HTTP_200_OK)