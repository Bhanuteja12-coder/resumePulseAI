from django.urls import path

from .views import JobDescriptionListCreateAPIView, JobDescriptionDetailAPIView

urlpatterns = [
    path("", JobDescriptionListCreateAPIView.as_view(), name="jobdescription-list-create"),
    path("<int:pk>/", JobDescriptionDetailAPIView.as_view(), name="jobdescription-detail"),
]
