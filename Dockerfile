FROM alpine:3.21

RUN apk add --no-cache \
    python3 \
    py3-pip \
    postgresql-dev \
    gcc \
    python3-dev \
    musl-dev \
    linux-headers \
    && python3 -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

WORKDIR /app

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
