from django.shortcuts import render

# class VagaList(APIView):
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *


class VagaList(APIView):
    def get(self, request):
        try:
            lista_vagas = Vaga.objects.all()
            paginator = PaginacaoVagas()
            result_page = paginator.paginate_queryset(lista_vagas, request)
            serializer = VagaSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = VagaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
