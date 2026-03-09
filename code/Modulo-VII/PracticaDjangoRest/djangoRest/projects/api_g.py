from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .data import Data
from .serializers import SumaSerializer, ProjectParameterSerializer
from django.core.serializers.json import DjangoJSONEncoder
import json

class DataTest(APIView):
    def get(self, request):
        dat = Data()
        return Response({"Resultado":dat.get_test_service()}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SumaSerializer(data=request.data)
        if serializer.is_valid():
            n1 = serializer._validated_data['num1']
            n2 = serializer._validated_data['num2']
            dat = Data()
            res = dat.get_suma(n1, n2)
            return Response({"Resultado":res}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectServices(APIView):
    def post(self, request):
        serializer = ProjectParameterSerializer(data=request.data)
        if serializer.is_valid():
            parameters = serializer.validated_data['parameters']
            dat = Data()
            res = dat.get_projects(parameters)
            res2 = json.dumps(list(res.values()), cls=DjangoJSONEncoder)
            return Response({"Resultado":res2}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

