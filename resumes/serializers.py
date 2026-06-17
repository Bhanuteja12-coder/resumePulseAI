import os

from rest_framework import serializers

from .models import AnalysisReport, Resume
from .utils import extract_skill_keywords, extract_gap_analysis, extract_text_from_file
from jobs.serializers import JobDescriptionSerializer


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ["id", "file", "extracted_text", "skill_keywords", "created_at"]


class AnalysisReportSerializer(serializers.ModelSerializer):
    resume = serializers.PrimaryKeyRelatedField(read_only=True)
    job_description = JobDescriptionSerializer(read_only=True)
    gap_analysis = serializers.SerializerMethodField(read_only=True)
    ai_suggestions = serializers.ListField(child=serializers.CharField(), read_only=True)

    class Meta:
        model = AnalysisReport
        fields = [
            "id",
            "resume",
            "job_description",
            "match_score",
            "match_percent",
            "gap_analysis",
            "ai_suggestions",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "resume",
            "job_description",
            "match_score",
            "match_percent",
            "gap_analysis",
            "ai_suggestions",
            "created_at",
        ]

    def get_gap_analysis(self, obj):
        return extract_gap_analysis(obj.resume.skill_keywords, obj.job_description.description or "")


class ResumeUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ["id", "user", "file", "extracted_text", "skill_keywords", "created_at"]
        read_only_fields = ["id", "user", "extracted_text", "skill_keywords", "created_at"]

    def validate_file(self, value):
        allowed_extensions = [".pdf", ".docx"]
        extension = os.path.splitext(value.name)[1].lower()
        if extension not in allowed_extensions:
            raise serializers.ValidationError("Only PDF and DOCX files are allowed.")
        return value

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        resume = super().create(validated_data)
        resume.extracted_text = extract_text_from_file(resume.file.path)
        resume.skill_keywords = extract_skill_keywords(resume.extracted_text)
        resume.save(update_fields=["extracted_text", "skill_keywords"])
        return resume
