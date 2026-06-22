from django.urls import path

from .views import ResumeAnalysisAPIView, ResumeDetailAPIView, ResumeListAPIView, ResumeSearchAPIView, ResumeUploadAPIView, AnalysisReportDeleteAPIView

urlpatterns = [
    path("upload/", ResumeUploadAPIView.as_view(), name="resume-upload"),
    path("upload", ResumeUploadAPIView.as_view()),
    path("analyze/", ResumeAnalysisAPIView.as_view(), name="resume-analyze"),
    path("analyze", ResumeAnalysisAPIView.as_view()),
    path("search/", ResumeSearchAPIView.as_view(), name="resume-search"),
    path("", ResumeListAPIView.as_view(), name="resume-list"),
    path("<int:pk>/", ResumeDetailAPIView.as_view(), name="resume-detail"),
    path(
        "reports/<int:pk>/delete/",
        AnalysisReportDeleteAPIView.as_view(),
        name="report-delete"
    ),
]
