# Конфиг Gunicorn (подхватывается автоматически из корня репозитория).
# Потоки позволяют одному воркеру обслуживать много ОДНОВРЕМЕННЫХ запросов,
# пока они ждут ответа (AI-запрос к OpenRouter длится до ~60с — это I/O-ожидание).
# gthread дёшев по памяти — важно для free-инстанса Render (512 МБ).
import os

worker_class = "gthread"
workers = int(os.environ.get("WEB_CONCURRENCY", "1"))
threads = int(os.environ.get("GUNICORN_THREADS", "8"))
timeout = 120          # длинные AI-ответы не убиваются по таймауту воркера
graceful_timeout = 30
keepalive = 5
