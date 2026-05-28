from django.contrib import admin
from .models import DocumentFieldValue, UserDocument


class DocumentFieldValueInline(admin.TabularInline):
    model = DocumentFieldValue
    extra = 0


@admin.register(UserDocument)
class UserDocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "status", "last_modified_at", "updated_at")
    list_filter = ("status", "template_version__template__document_type__domain")
    search_fields = ("title", "user__email")
    inlines = [DocumentFieldValueInline]
