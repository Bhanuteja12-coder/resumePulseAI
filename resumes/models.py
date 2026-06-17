from django.conf import settings
from django.db import models


def resume_upload_path(instance, filename):
    return f"resumes/{instance.user.id}/{filename}"


class Resume(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="resumes",
    )
    file = models.FileField(upload_to=resume_upload_path)
    extracted_text = models.TextField(blank=True)
    skill_keywords = models.JSONField(blank=True, default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Resume({self.user.email})"


class AnalysisReport(models.Model):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name="analysis_reports",
    )
    job_description = models.ForeignKey(
        "jobs.JobDescription",
        on_delete=models.CASCADE,
        related_name="analysis_reports",
    )
    match_score = models.FloatField()
    match_percent = models.FloatField()
    ai_suggestions = models.JSONField(blank=True, default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"AnalysisReport(resume={self.resume.id}, job={self.job_description.id}, score={self.match_percent}%)"
