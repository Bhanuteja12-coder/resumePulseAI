from rest_framework import generics, permissions

from .serializers import ResumeUploadSerializer


class ResumeUploadAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ResumeUploadSerializer
