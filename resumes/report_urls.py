from django.urls import path

from .views import AnalysisReportDetailAPIView, AnalysisReportListAPIView

urlpatterns = [
    path('', AnalysisReportListAPIView.as_view(), name='report-list'),
    path('<int:pk>/', AnalysisReportDetailAPIView.as_view(), name='report-detail'),
]
