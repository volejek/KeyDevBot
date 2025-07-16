from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArrivalRecordSerializer


class ArrivalRecordViewSet(APIView):
    """
    ViewSet for handling ArrivalRecord operations.
    """
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = ArrivalRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(f"Validation errors: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    