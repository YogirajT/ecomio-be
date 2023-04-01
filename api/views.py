from rest_framework.response import Response
from rest_framework import status, generics
from api.models import DestinationModel, SearchDataModel
from api.serializers import DestinationSerializer, SearchDataSerializer
import math
from datetime import datetime


class Destination(generics.GenericAPIView):
    serializer_class = DestinationSerializer
    queryset = DestinationModel.objects.all()

    def get(self, request):
        destinations = DestinationModel.objects.all()
        total = destinations.count()
        serializer = self.serializer_class(destinations, many=True)
        return Response({
            "destinations": serializer.data,
            "total": total
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "note": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class SearchData(generics.GenericAPIView):
    queryset = SearchDataModel.objects.all()
    serializer_class = SearchDataSerializer

    def get(self, request):
        search_data = SearchDataModel.objects.all()
        total = search_data.count()
        serializer = self.serializer_class(search_data, many=True)
        return Response({
            "search_data": serializer.data,
            "total": total
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "note": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

