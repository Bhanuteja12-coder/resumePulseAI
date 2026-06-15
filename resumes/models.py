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
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Resume({self.user.email})"
