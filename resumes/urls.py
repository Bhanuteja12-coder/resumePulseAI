from django.urls import path

from .views import ResumeDetailAPIView, ResumeListAPIView, ResumeUploadAPIView

urlpatterns = [
    path("upload/", ResumeUploadAPIView.as_view(), name="resume-upload"),
    path("", ResumeListAPIView.as_view(), name="resume-list"),
    path("<int:pk>/", ResumeDetailAPIView.as_view(), name="resume-detail"),
]
