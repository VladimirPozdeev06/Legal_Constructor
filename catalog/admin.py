from django.contrib import admin
from .models import DocumentType, LegalDomain, Template, TemplateAttachment, TemplateVersion


@admin.register(LegalDomain)
class LegalDomainAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "sort_order")
    list_editable = ("is_active", "sort_order")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "domain", "is_active", "sort_order")
    list_filter = ("domain", "is_active")
    list_editable = ("is_active", "sort_order")
    search_fields = ("name", "short_description", "keywords")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ("title", "document_type", "is_active", "created_at")
    list_filter = ("is_active", "document_type")
    search_fields = ("title",)


class TemplateAttachmentInline(admin.TabularInline):
    model = TemplateAttachment
    extra = 1
    fields = ('title', 'docx_file', 'sort_order')


@admin.register(TemplateVersion)
class TemplateVersionAdmin(admin.ModelAdmin):
    list_display = ("template", "version_number", "is_published", "has_docx", "attachments_count", "created_at")
    list_filter = ("is_published",)
    search_fields = ("template__title",)
    readonly_fields = ("created_at",)
    fields = ("template", "version_number", "is_published", "docx_file", "body", "created_at")
    inlines = [TemplateAttachmentInline]

    @admin.display(boolean=True, description="Есть docx")
    def has_docx(self, obj):
        return bool(obj.docx_file)

    @admin.display(description="Приложений")
    def attachments_count(self, obj):
        return obj.attachments.count()


@admin.register(TemplateAttachment)
class TemplateAttachmentAdmin(admin.ModelAdmin):
    list_display = ("title", "template_version", "sort_order")
    list_filter = ("template_version__template__document_type",)
    search_fields = ("title",)
