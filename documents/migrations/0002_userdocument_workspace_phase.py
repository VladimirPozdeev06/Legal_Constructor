from django.db import migrations, models


def set_existing_to_editing(apps, schema_editor):
    UserDocument = apps.get_model("documents", "UserDocument")
    UserDocument.objects.all().update(workspace_phase="editing")


class Migration(migrations.Migration):
    dependencies = [
        ("documents", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userdocument",
            name="workspace_phase",
            field=models.CharField(
                max_length=20,
                choices=[
                    ("variables", "Переменные"),
                    ("editing", "Редактирование"),
                ],
                default="variables",
            ),
        ),
        migrations.RunPython(set_existing_to_editing, migrations.RunPython.noop),
    ]
