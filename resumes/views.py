from rest_framework import generics, permissions, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .models import AnalysisReport, Resume
from .serializers import AnalysisReportSerializer, ResumeUploadSerializer, ResumeSerializer
from .utils import extract_gap_analysis, generate_gemini_suggestions
from jobs.models import JobDescription


class ResumeUploadAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ResumeUploadSerializer


class ResumeListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ResumeSerializer

    def get_queryset(self):
        return Resume.objects.filter(user=self.request.user)


class ResumeSearchAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ResumeSerializer

    def get_queryset(self):
        query = self.request.query_params.get("skill", "").strip().lower()
        qs = Resume.objects.filter(user=self.request.user)
        if not query:
            return qs.none()
        return qs.filter(skill_keywords__contains=[query])


class ReportPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50


class AnalysisReportListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AnalysisReportSerializer
    pagination_class = ReportPagination

    def get_queryset(self):
        return AnalysisReport.objects.filter(
            resume__user=self.request.user
        ).select_related("resume", "job_description").order_by("-created_at")


class AnalysisReportDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AnalysisReportSerializer

    def get_queryset(self):
        return AnalysisReport.objects.filter(
            resume__user=self.request.user
        ).select_related("resume", "job_description")


class ResumeAnalysisAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AnalysisReportSerializer

    def create(self, request, *args, **kwargs):
        resume_id = request.data.get("resume_id")
        job_description_id = request.data.get("job_description_id")
        if not resume_id or not job_description_id:
            return Response(
                {"detail": "resume_id and job_description_id are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            resume = Resume.objects.get(pk=resume_id, user=request.user)
        except Resume.DoesNotExist:
            return Response(
                {"detail": "Resume not found or does not belong to the current user."},
                status=status.HTTP_404_NOT_FOUND,
            )

        try:
            job_description = JobDescription.objects.get(pk=job_description_id)
        except JobDescription.DoesNotExist:
            return Response(
                {"detail": "Job description not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        resume_text = resume.extracted_text or ""
        job_text = job_description.description or ""
        vectorizer = TfidfVectorizer(stop_words="english")
        try:
            tfidf = vectorizer.fit_transform([resume_text, job_text])
            if tfidf.shape[1] == 0:
                score = 0.0
            else:
                score = float(cosine_similarity(tfidf[0], tfidf[1])[0][0])
        except ValueError:
            score = 0.0

        gap_analysis = extract_gap_analysis(resume.skill_keywords, job_text)
        ai_suggestions = generate_gemini_suggestions(job_text, gap_analysis)

        report = AnalysisReport.objects.create(
            resume=resume,
            job_description=job_description,
            match_score=score,
            match_percent=round(score * 100, 2),
            ai_suggestions=ai_suggestions,
        )
        serializer = self.get_serializer(report)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ResumeDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ResumeSerializer

    def get_queryset(self):
        return Resume.objects.filter(user=self.request.user)
