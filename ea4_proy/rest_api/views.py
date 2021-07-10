from rest_api.serializers import ObraSerializer
from core_app.models import Obra
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# agregar el decorador sobre los def
@permission_classes((IsAuthenticated,))
@api_view(['GET', 'POST'])
def obras_api (request):
    if request.method=='GET':
        lista_obra = Obra.objects.all()
        serializer = ObraSerializer(lista_obra, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data =  JSONParser().parse(request)
        serializer = ObraSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes((IsAuthenticated,))
@api_view(['GET', 'PUT', 'DELETE'])
def obra_api(request, pk):
    try:
        obra = Obra.objects.get(idObra=pk)
    except Obra.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ObraSerializer(obra)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ObraSerializer(obra, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':

        obra.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)