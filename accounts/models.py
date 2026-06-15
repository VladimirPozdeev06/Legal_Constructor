from django.conf import settings
from django.db import models


class AIUsage(models.Model):
    """Счётчик израсходованных запросов к AI-помощнику на пользователя (на всё время).
    Хранится в БД, поэтому переживает перезапуски сайта."""
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="ai_usage",
    )
    used = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} — использовано {self.used}"
