FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libmariadb-dev \
    pkg-config \
    libzmq3-dev \
    gcc \
    make \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install -r requirements.txt

ENV PATH="/opt/venv/bin:$PATH"

COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
