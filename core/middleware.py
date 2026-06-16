"""Дополнительные security-заголовки (Content-Security-Policy и пр.)."""


class SecurityHeadersMiddleware:
    """Добавляет Content-Security-Policy ко всем ответам.

    Источники ограничены тем, что реально использует сайт: собственный домен,
    Google Fonts и Tailwind Play CDN. Tailwind CDN компилирует стили в браузере,
    поэтому для script/style нужны 'unsafe-inline'/'unsafe-eval' — строже без
    отказа от CDN (переход на собранный Tailwind) не получится.
    """

    CSP = (
        "default-src 'self'; "
        "script-src 'self' https://cdn.tailwindcss.com 'unsafe-inline' 'unsafe-eval'; "
        "style-src 'self' https://fonts.googleapis.com 'unsafe-inline'; "
        "font-src 'self' https://fonts.gstatic.com; "
        "img-src 'self' data:; "
        "connect-src 'self'; "
        "frame-ancestors 'none'; "
        "base-uri 'self'; "
        "form-action 'self'"
    )

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response.setdefault("Content-Security-Policy", self.CSP)
        return response
