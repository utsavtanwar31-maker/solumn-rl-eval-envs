FROM python:3.11-slim@sha256:d8b28d6896265012586e33f0017a54a72d427d6d3d4bfaeb4566c3c86c12217c

WORKDIR /app

RUN pip install --no-cache-dir pytest

COPY src/ /app/

ENV PYTHONPATH=/app
