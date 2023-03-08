from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import bookserializer
from .models import books
# Create your views here.

class listviewApi(APIView):
    def get(self, request):
        queryset = books.objects.all()
        ser = bookserializer(queryset, many=True)
        return Response(ser.data)

class detailviewApi(APIView):
    def get(self, request, pk):
        queryset = books.objects.get(pk=pk)
        ser = bookserializer(queryset)
        return Response(ser.data)


class addbookApi(APIView):
    def post(self, request):
        data_ser = bookserializer(data=request.data)
        if data_ser.is_valid():
            data_ser.save()
            return Response({'massage': 'down'})
        return Response(data_ser.errors)
