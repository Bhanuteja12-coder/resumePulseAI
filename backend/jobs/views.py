from rest_framework import generics, permissions

from .models import JobDescription
from .serializers import JobDescriptionSerializer


class JobDescriptionListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = JobDescription.objects.all()
    serializer_class = JobDescriptionSerializer


class JobDescriptionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = JobDescription.objects.all()
    serializer_class = JobDescriptionSerializer
