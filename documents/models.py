from django.db import models
from django.conf import settings
from django.utils import timezone

from catalog.models import TemplateVersion


class UserDocument(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Черновик"
        READY = "ready", "Готов"
        ARCHIVED = "archived", "Архив"
        DELETED = "deleted", "Удален"

    class WorkspacePhase(models.TextChoices):
        VARIABLES = "variables", "Переменные"
        EDITING = "editing", "Редактирование"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="documents"
    )
    template_version = models.ForeignKey(
        TemplateVersion, on_delete=models.PROTECT, related_name="user_documents"
    )
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    workspace_phase = models.CharField(
        max_length=20,
        choices=WorkspacePhase.choices,
        default=WorkspacePhase.VARIABLES,
    )
    content = models.TextField(blank=True)
    last_modified_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return f"{self.title} ({self.user.email})"


class DocumentFieldValue(models.Model):
    user_document = models.ForeignKey(
        UserDocument, on_delete=models.CASCADE, related_name="field_values"
    )
    variable_key = models.CharField(max_length=120)
    variable_label = models.CharField(max_length=180, blank=True)
    value = models.TextField(blank=True)
    is_required = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["variable_key"]
        unique_together = [("user_document", "variable_key")]

    def __str__(self):
        return f"{self.variable_key} -> {self.user_document_id}"
