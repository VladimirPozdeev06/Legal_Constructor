from django.db import models


class LegalDomain(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True)
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "name"]

    def __str__(self):
        return self.name


class DocumentType(models.Model):
    domain = models.ForeignKey(
        LegalDomain, on_delete=models.CASCADE, related_name="document_types"
    )
    name = models.CharField(max_length=180)
    slug = models.SlugField(max_length=200)
    short_description = models.CharField(max_length=255, blank=True)
    keywords = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "name"]
        unique_together = [("domain", "slug")]

    def __str__(self):
        return self.name


class Template(models.Model):
    document_type = models.ForeignKey(
        DocumentType, on_delete=models.CASCADE, related_name="templates"
    )
    title = models.CharField(max_length=180)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class TemplateVersion(models.Model):
    template = models.ForeignKey(
        Template, on_delete=models.CASCADE, related_name="versions"
    )
    version_number = models.PositiveIntegerField()
    body = models.TextField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-version_number"]
        unique_together = [("template", "version_number")]

    def __str__(self):
        return f"{self.template.title} v{self.version_number}"
