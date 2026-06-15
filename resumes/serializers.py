import os

from rest_framework import serializers

from .models import Resume
from .utils import extract_text_from_file


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ["id", "file", "extracted_text", "created_at"]


class ResumeUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ["id", "user", "file", "extracted_text", "created_at"]
        read_only_fields = ["id", "user", "extracted_text", "created_at"]

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
        resume.save(update_fields=["extracted_text"])
        return resume
