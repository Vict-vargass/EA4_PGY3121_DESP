from rest_api.serializers import ObraSerializer
from core_app.models import Obra
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def obra_api (request):
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

