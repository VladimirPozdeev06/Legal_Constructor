from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("cabinet/", views.cabinet, name="cabinet"),
    path("my-documents/", views.my_documents, name="my_documents"),
    path(
        "document-types/<int:document_type_id>/download-docx/",
        views.download_template_docx,
        name="download_template_docx",
    ),
    path(
        "document-types/<int:document_type_id>/fill/",
        views.fill_docx_form,
        name="fill_docx_form",
    ),
    path(
        "document-types/<int:document_type_id>/start/",
        views.start_document,
        name="start_document",
    ),
    path(
        "documents/<int:doc_id>/export-docx/",
        views.download_user_document_docx,
        name="download_user_document_docx",
    ),
    path(
        "documents/<int:doc_id>/save-fields/",
        views.save_document_fields,
        name="save_document_fields",
    ),
    path(
        "documents/<int:doc_id>/finalize-variables/",
        views.finalize_variables,
        name="finalize_variables",
    ),
    path(
        "documents/<int:doc_id>/save-editor/",
        views.save_document_editor,
        name="save_document_editor",
    ),
    path(
        "documents/<int:doc_id>/duplicate/",
        views.duplicate_document,
        name="duplicate_document",
    ),
    path(
        "documents/<int:doc_id>/delete/",
        views.delete_document,
        name="delete_document",
    ),
    path("api/ai/search/", views.ai_search_documents, name="ai_search_documents"),
    path("api/ai/ask/", views.ai_ask_llm, name="ai_ask_llm"),
    path("api/ai/quota/", views.ai_quota, name="ai_quota"),
    path("legal/preview/<slug:slug>/", views.legal_document_preview, name="legal_document_preview"),
]
