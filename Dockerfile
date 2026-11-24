FROM python:3.12.12-slim-bookworm
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1 BOTHOST_MODE=1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && useradd --system --uid 10001 mio
COPY main.py mio_dungeons.bundle ./
USER 10001
EXPOSE 8080
CMD ["python", "main.py"]
