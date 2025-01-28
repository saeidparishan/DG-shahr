from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import TodoitemSerializer
from . models import Todoitem

# CRUD Create, Retirive, Update, Delete
class TodoListView(APIView):

    # Retrieve all Todo items
    def get(self, request):
        todos = Todoitem.objects.all()
        serializer = TodoitemSerializer(todos, many=True)
        return Response(serializer.data)
    
    # Create a new Todo item
    def post(self, request):
        serializer = TodoitemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TodoitemDetailView(APIView):

    def get_object(self, pk):
        try:
            todoitem = Todoitem.objects.get(pk=pk)
        except Todoitem.DoesNotExist:
            raise Http404
        return todoitem
    
    # Retrieve a Todo item by ID
    def get(self,request,pk):
        todoitem = self.get_object(pk)
        serializer = TodoitemSerializer(todoitem)
        return Response(serializer.data)
    
    # Update a Todo item by ID
    def put(self, request, pk):  
        todoitem = self.get_object(pk)   
        serializer = TodoitemSerializer(todoitem, data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_200_OK)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    # Delete a Todo item by ID
    def delete(self, request, pk):  
        todoitem = self.get_object(pk)  
        todoitem.delete()  
        return Response(status=status.HTTP_204_NO_CONTENT)
        

