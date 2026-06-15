import os

from rest_framework import serializers

from .models import Resume


class ResumeUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ["id", "user", "file", "created_at"]
        read_only_fields = ["id", "user", "created_at"]

    def validate_file(self, value):
        allowed_extensions = [".pdf", ".docx"]
        extension = os.path.splitext(value.name)[1].lower()
        if extension not in allowed_extensions:
            raise serializers.ValidationError("Only PDF and DOCX files are allowed.")
        return value

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
